"""赛事管理接口"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db import get_db
from app.models import Competition, User

router = APIRouter(prefix="/competitions", tags=["competitions"])


@router.get("", response_model=List[dict])
async def list_competitions(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    """获取赛事列表"""
    result = await db.execute(
        select(Competition).offset(skip).limit(limit)
    )
    competitions = result.scalars().all()
    return [
        {
            "id": c.id,
            "name": c.name,
            "competition_type": c.competition_type,
            "season": c.season,
            "start_date": c.start_date,
            "end_date": c.end_date,
        }
        for c in competitions
    ]


@router.get("/{competition_id}", response_model=dict)
async def get_competition(
    competition_id: int,
    db: AsyncSession = Depends(get_db),
):
    """获取赛事详情"""
    result = await db.execute(
        select(Competition).where(Competition.id == competition_id)
    )
    competition = result.scalar_one_or_none()
    if not competition:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Competition not found",
        )
    return {
        "id": competition.id,
        "name": competition.name,
        "competition_type": competition.competition_type,
        "season": competition.season,
        "description": competition.description,
        "start_date": competition.start_date,
        "end_date": competition.end_date,
        "rules": competition.rules,
    }


@router.post("", response_model=dict)
async def create_competition(
    data: dict,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """创建赛事"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )

    competition = Competition(**data)
    db.add(competition)
    await db.commit()
    await db.refresh(competition)
    
    return {
        "id": competition.id,
        "name": competition.name,
        "competition_type": competition.competition_type,
        "season": competition.season,
    }
