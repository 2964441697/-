"""球员数据模型"""
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime, date


class HealthRecordBase(BaseModel):
    record_type: str
    description: str
    start_date: date
    end_date: Optional[date] = None
    status: str = "进行中"
    notes: Optional[str] = None


class HealthRecord(HealthRecordBase):
    id: int
    player_id: int

    class Config:
        from_attributes = True


class PlayerStatisticsBase(BaseModel):
    season: str
    appearance: int = 0
    goals: int = 0
    assists: int = 0
    yellow_cards: int = 0
    red_cards: int = 0
    minutes_played: int = 0


class PlayerStatistics(PlayerStatisticsBase):
    id: int
    player_id: int

    class Config:
        from_attributes = True


class PlayerBase(BaseModel):
    name: str
    team_id: int
    position: str
    jersey_number: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    birth_date: Optional[date] = None
    nationality: Optional[str] = None
    biography: Optional[str] = None


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    jersey_number: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    birth_date: Optional[date] = None
    nationality: Optional[str] = None
    biography: Optional[str] = None
    photo: Optional[str] = None


class Player(PlayerBase):
    id: int
    photo: Optional[str] = None
    created_at: datetime
    statistics: List[PlayerStatistics] = []
    health_records: List[HealthRecord] = []

    class Config:
        from_attributes = True
