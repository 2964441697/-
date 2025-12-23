"""球队数据模型"""
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class HonorBase(BaseModel):
    title: str
    year: int
    description: Optional[str] = None
    image: Optional[str] = None


class Honor(HonorBase):
    id: int
    team_id: int

    class Config:
        from_attributes = True


class TeamBase(BaseModel):
    name: str
    home_ground: Optional[str] = None
    founded_year: Optional[int] = None
    description: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class TeamUpdate(BaseModel):
    name: Optional[str] = None
    home_ground: Optional[str] = None
    founded_year: Optional[int] = None
    description: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    logo: Optional[str] = None


class Team(TeamBase):
    id: int
    logo: Optional[str] = None
    created_at: datetime
    honors: List[Honor] = []

    class Config:
        from_attributes = True


class TeamWithStats(Team):
    player_count: int = 0
    total_wins: int = 0
    total_losses: int = 0
