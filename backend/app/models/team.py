"""球队模型"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Team(Base):
    """球队模型"""

    __tablename__ = "team"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    logo = Column(String(255), nullable=True)
    home_ground = Column(String(100), nullable=True)
    founded_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    players = relationship("Player", back_populates="team", cascade="all, delete-orphan")
    honors = relationship("Honor", back_populates="team", cascade="all, delete-orphan")
    match_records = relationship(
        "MatchRecord", back_populates="home_team", foreign_keys="MatchRecord.home_team_id"
    )

    def __repr__(self):
        return f"<Team {self.name}>"


class Honor(Base):
    """荣誉记录模型"""

    __tablename__ = "honor"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("team.id"))
    title = Column(String(100))
    description = Column(Text, nullable=True)
    image = Column(String(255), nullable=True)
    year = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    team = relationship("Team", back_populates="honors")

    def __repr__(self):
        return f"<Honor {self.title}>"
