"""训练管理模型"""
from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class TrainingPlan(Base):
    """训练计划模型"""

    __tablename__ = "training_plan"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("team.id"))
    coach_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String(100))
    topic = Column(String(100))  # 主题
    description = Column(Text, nullable=True)
    scheduled_date = Column(Date)
    scheduled_time = Column(Time, nullable=True)
    duration = Column(Integer, nullable=True)  # 时长（分钟）
    location = Column(String(100), nullable=True)
    category = Column(String(50))  # 分类：体能、技术、战术、恢复
    status = Column(String(50), default="scheduled")  # 状态：待定、进行中、已完成、已取消
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    team = relationship("Team")
    coach = relationship("User")
    records = relationship(
        "TrainingRecord", back_populates="plan", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<TrainingPlan {self.title}>"


class TrainingRecord(Base):
    """训练记录模型"""

    __tablename__ = "training_record"

    id = Column(Integer, primary_key=True, index=True)
    training_plan_id = Column(Integer, ForeignKey("training_plan.id"))
    player_id = Column(Integer, ForeignKey("player.id"))
    attendance = Column(String(50))  # 参与情况：出席、缺席、迟到
    completion_rate = Column(Integer, nullable=True)  # 完成度（百分比）
    performance_score = Column(Integer, nullable=True)  # 表现评分（1-10）
    coach_comment = Column(Text, nullable=True)  # 教练评论
    recorded_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    plan = relationship("TrainingPlan", back_populates="records")
    player = relationship("Player")

    def __repr__(self):
        return f"<TrainingRecord Player {self.player_id}>"


class TrainingResource(Base):
    """训练资源模型"""

    __tablename__ = "training_resource"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("team.id"))
    resource_type = Column(String(50))  # 类型：教案、视频、器材、其他
    name = Column(String(100))
    description = Column(Text, nullable=True)
    file_path = Column(String(255), nullable=True)
    file_url = Column(String(255), nullable=True)
    category = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<TrainingResource {self.name}>"
