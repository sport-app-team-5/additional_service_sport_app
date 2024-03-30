from __future__ import annotations
from sqlalchemy import DateTime, ForeignKey, String, CHAR
from datetime import datetime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List
from app.config.db import Base


class PermissionRole(Base):
    __tablename__ = "permission_roles"
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True, index=True)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id"), primary_key=True, index=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    permission: Mapped["Permission"] = relationship(back_populates="roles")
    role: Mapped["Role"] = relationship(back_populates="permissions")


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(CHAR(4), unique=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    permissions: Mapped[List["PermissionRole"]] = relationship(back_populates="role")

    def __str__(self):
        return self.name


class Permission(Base):
    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    action: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(CHAR(4), unique=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    roles: Mapped[List["PermissionRole"]] = relationship(back_populates="permission")

    def __str__(self):
        return self.name
