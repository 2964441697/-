"""球员管理接口"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db import get_db
from app.models import Player, User
from app.schemas import Player as PlayerSchema, PlayerCreate, PlayerUpdate

router = APIRouter(prefix="/players", tags=["players"])


@router.get("", response_model=List[PlayerSchema])
async def list_players(
    team_id: int = None,
    position: str = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    """获取球员列表"""
    query = select(Player)
    
    if team_id:
        query = query.where(Player.team_id == team_id)
    if position:
        query = query.where(Player.position == position)
    
    result = await db.execute(query.offset(skip).limit(limit))
    players = result.scalars().all()
    return players


@router.get("/{player_id}", response_model=PlayerSchema)
async def get_player(
    player_id: int,
    db: AsyncSession = Depends(get_db),
):
    """获取球员详情"""
    result = await db.execute(
        select(Player).where(Player.id == player_id)
    )
    player = result.scalar_one_or_none()
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found",
        )
    return player


@router.post("", response_model=PlayerSchema)
async def create_player(
    player_data: PlayerCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """创建球员"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )

    player = Player(**player_data.dict())
    db.add(player)
    await db.commit()
    await db.refresh(player)
    return player


@router.put("/{player_id}", response_model=PlayerSchema)
async def update_player(
    player_id: int,
    player_data: PlayerUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """更新球员"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )

    result = await db.execute(
        select(Player).where(Player.id == player_id)
    )
    player = result.scalar_one_or_none()
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found",
        )

    update_data = player_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(player, field, value)

    await db.commit()
    await db.refresh(player)
    return player


@router.delete("/{player_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(
    player_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """删除球员"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )

    result = await db.execute(
        select(Player).where(Player.id == player_id)
    )
    player = result.scalar_one_or_none()
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found",
        )

    await db.delete(player)
    await db.commit()
