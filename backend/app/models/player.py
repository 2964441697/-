"""球员模型"""
from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class Player(Base):
    """球员模型"""

    __tablename__ = "player"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("team.id"))
    jersey_number = Column(Integer, nullable=True)
    name = Column(String(100), index=True)
    position = Column(String(50))  # 位置：门将、后卫、中场、前锋
    height = Column(Float, nullable=True)  # 身高（cm）
    weight = Column(Float, nullable=True)  # 体重（kg）
    birth_date = Column(Date, nullable=True)
    nationality = Column(String(50), nullable=True)
    photo = Column(String(255), nullable=True)
    biography = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    team = relationship("Team", back_populates="players")
    statistics = relationship(
        "PlayerStatistics", back_populates="player", cascade="all, delete-orphan"
    )
    health_records = relationship(
        "HealthRecord", back_populates="player", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Player {self.name}>"


class PlayerStatistics(Base):
    """球员统计模型"""

    __tablename__ = "player_statistics"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.id"))
    season = Column(String(20))  # 赛季
    appearance = Column(Integer, default=0)  # 出场次数
    goals = Column(Integer, default=0)  # 进球数
    assists = Column(Integer, default=0)  # 助攻数
    yellow_cards = Column(Integer, default=0)  # 黄牌
    red_cards = Column(Integer, default=0)  # 红牌
    minutes_played = Column(Integer, default=0)  # 出场时间（分钟）
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    player = relationship("Player", back_populates="statistics")

    def __repr__(self):
        return f"<PlayerStatistics {self.season}>"


class HealthRecord(Base):
    """健康记录模型"""

    __tablename__ = "health_record"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.id"))
    record_type = Column(String(50))  # 类型：伤病、体检、康复
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    status = Column(String(50))  # 状态：进行中、已完成、已取消
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    player = relationship("Player", back_populates="health_records")

    def __repr__(self):
        return f"<HealthRecord {self.record_type}>"
