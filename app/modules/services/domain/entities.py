from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import Float, String, DateTime, Boolean, ForeignKey, Integer
from app.config.db import Base
from app.modules.third_party.domain.entities import ThirdParty


class Service(Base):
    __tablename__ = 'service'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    third_party_id: Mapped[int] = mapped_column(ForeignKey("third_party.id"), index=True)
    is_inside_house: Mapped[bool] = mapped_column(Boolean)
    type: Mapped[Optional[str]] = mapped_column(String(30))
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
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    third: Mapped["ThirdParty"] = relationship()
    sport: Mapped["Sport"] = relationship()

    def __str__(self):
        return self.name


class Sport(Base):
    __tablename__ = "sport"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(5), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return self.name
    
class EventSportman(Base):
    __tablename__ = 'event_sportman'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    event_id: Mapped[int] =  mapped_column(ForeignKey("event.id"), index=True)
    sportman_id: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    event: Mapped["Event"] = relationship()
    def __str__(self):
        return self.name

class ServiceSportman(Base):
    __tablename__ = 'service_sportman'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    service_id: Mapped[int] =  mapped_column(ForeignKey("service.id"), index=True)
    sportman_id: Mapped[int] = mapped_column(Integer)
    sport: Mapped[str] = mapped_column(String(30))
    injury_id: Mapped[int] = mapped_column(Integer)
    appointment_date: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    service: Mapped["Service"] = relationship()
    def __str__(self):
        return self.name
    
class Notification(Base):
    __tablename__ = 'notification'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    message: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(30))    
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return self.name    