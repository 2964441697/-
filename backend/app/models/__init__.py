"""模型模块"""
from app.models.user import User, Role, Permission
from app.models.team import Team, Honor
from app.models.player import Player, PlayerStatistics, HealthRecord
from app.models.match import Competition, Schedule, MatchRecord, Standing
from app.models.training import TrainingPlan, TrainingRecord, TrainingResource

__all__ = [
    "User",
    "Role",
    "Permission",
    "Team",
    "Honor",
    "Player",
    "PlayerStatistics",
    "HealthRecord",
    "Competition",
    "Schedule",
    "MatchRecord",
    "Standing",
    "TrainingPlan",
    "TrainingRecord",
    "TrainingResource",
]
