"""赛事和比赛模型"""
from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class Competition(Base):
    """赛事配置模型"""

    __tablename__ = "competition"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    competition_type = Column(String(50))  # 类型：联赛、杯赛
    season = Column(String(20))  # 赛季
    description = Column(Text, nullable=True)
    start_date = Column(Date)
    end_date = Column(Date)
    rules = Column(Text, nullable=True)  # 积分/晋级规则
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    schedules = relationship(
        "Schedule", back_populates="competition", cascade="all, delete-orphan"
    )
    standings = relationship(
        "Standing", back_populates="competition", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Competition {self.name}>"


class Schedule(Base):
    """赛程模型"""

    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)
    competition_id = Column(Integer, ForeignKey("competition.id"))
    round_number = Column(Integer)  # 轮次
    match_date = Column(Date)
    match_time = Column(Time, nullable=True)
    home_team_id = Column(Integer, ForeignKey("team.id"))
    away_team_id = Column(Integer, ForeignKey("team.id"))
    venue = Column(String(100), nullable=True)
    status = Column(String(50))  # 状态：待定、进行中、已完成、已取消
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    competition = relationship("Competition", back_populates="schedules")
    match_record = relationship(
        "MatchRecord", back_populates="schedule", uselist=False, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Schedule Round {self.round_number}>"


class MatchRecord(Base):
    """比赛记录模型"""

    __tablename__ = "match_record"

    id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey("schedule.id"))
    home_team_id = Column(Integer, ForeignKey("team.id"))
    away_team_id = Column(Integer, ForeignKey("team.id"))
    home_goals = Column(Integer, default=0)
    away_goals = Column(Integer, default=0)
    status = Column(String(50))  # 状态：进行中、已完成
    event_details = Column(Text, nullable=True)  # JSON格式的事件详情
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    schedule = relationship("Schedule", back_populates="match_record")
    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])

    def __repr__(self):
        return f"<MatchRecord {self.home_goals}-{self.away_goals}>"


class Standing(Base):
    """积分榜模型"""

    __tablename__ = "standing"

    id = Column(Integer, primary_key=True, index=True)
    competition_id = Column(Integer, ForeignKey("competition.id"))
    team_id = Column(Integer, ForeignKey("team.id"))
    rank = Column(Integer)
    played = Column(Integer, default=0)  # 比赛场数
    won = Column(Integer, default=0)  # 胜场数
    drawn = Column(Integer, default=0)  # 平局次数
    lost = Column(Integer, default=0)  # 负场数
    goals_for = Column(Integer, default=0)  # 进球数
    goals_against = Column(Integer, default=0)  # 失球数
    goal_difference = Column(Integer, default=0)  # 净胜球
    points = Column(Integer, default=0)  # 积分
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    competition = relationship("Competition", back_populates="standings")
    team = relationship("Team")

    def __repr__(self):
        return f"<Standing Rank {self.rank}>"
