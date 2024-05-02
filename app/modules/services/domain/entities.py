from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import Float, String, DateTime, Boolean, ForeignKey, Integer
from app.config.db import Base
from app.modules.third_party.domain.entities import ThirdParty


class Service(Base):
    __tablename__ = 'service'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    third_party_id: Mapped[int] = mapped_column(ForeignKey("third_party.id"), index=True)
    type: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(512))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    cost: Mapped[float] = mapped_column(Float)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    third: Mapped["ThirdParty"] = relationship()

    def __str__(self):
        return self.description


class Event(Base):
    __tablename__ = 'event'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    third_party_id: Mapped[int] = mapped_column(ForeignKey("third_party.id"), index=True)
    city_id: Mapped[int] = mapped_column(Integer)
    sport_id: Mapped[int] = mapped_column(ForeignKey("sport.id"), index=True)
    location: Mapped[str] = mapped_column(String(150))
    date: Mapped[str] = mapped_column(String(30))
    capacity: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(256))
    type: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    third: Mapped["ThirdParty"] = relationship()
    sport: Mapped["Sport"] = relationship()

    def __str__(self):
        return self.description


class Sport(Base):
    __tablename__ = "sport"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(5), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return self.name
