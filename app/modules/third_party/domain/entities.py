from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, DateTime, Boolean, ForeignKey, Integer
from app.config.db import Base
from app.modules.auth.domain.entities import Role


class ThirdParty(Base):
    __tablename__ = 'third_party'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    city_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer) 
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return self.name