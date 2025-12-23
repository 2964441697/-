"""用户模型"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base

# 用户-角色关联表
user_role_association = Table(
    "user_role",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("role_id", Integer, ForeignKey("role.id")),
)


class User(Base):
    """用户模型"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    full_name = Column(String(100))
    phone = Column(String(20), nullable=True)
    avatar = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)

    # 关系
    roles = relationship(
        "Role",
        secondary=user_role_association,
        back_populates="users",
        cascade="save-update",
    )

    def __repr__(self):
        return f"<User {self.username}>"


class Role(Base):
    """角色模型"""

    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), nullable=True)
    is_system = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    users = relationship(
        "User", secondary=user_role_association, back_populates="roles"
    )
    permissions = relationship(
        "Permission",
        secondary="role_permission",
        back_populates="roles",
        cascade="save-update",
    )

    def __repr__(self):
        return f"<Role {self.name}>"


class Permission(Base):
    """权限模型"""

    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), nullable=True)
    resource = Column(String(50))  # 资源名称
    action = Column(String(50))  # 操作 (create, read, update, delete)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 关系
    roles = relationship(
        "Role", secondary="role_permission", back_populates="permissions"
    )

    def __repr__(self):
        return f"<Permission {self.name}>"


# 角色-权限关联表
role_permission_association = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("permission_id", Integer, ForeignKey("permission.id")),
)
