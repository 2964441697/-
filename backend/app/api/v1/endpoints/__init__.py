"""API端点模块"""
from app.api.v1.endpoints import auth, teams, players, competitions

__all__ = ["auth", "teams", "players", "competitions"]
