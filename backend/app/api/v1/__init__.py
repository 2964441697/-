"""API v1 模块"""
from fastapi import APIRouter
from app.api.v1.endpoints import auth, teams, players, competitions

router = APIRouter(prefix="/api/v1")

# 注册路由
router.include_router(auth.router)
router.include_router(teams.router)
router.include_router(players.router)
router.include_router(competitions.router)

__all__ = ["router"]
