from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, DateTime, Boolean, ForeignKey, Integer
from app.config.db import Base
from app.modules.auth.domain.entities import Role


class ThirdParty(Base):
    __tablename__ = 'third_party'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    city_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer) 
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    services: Mapped["Service"] = relationship(back_populates="service")
    products: Mapped["Product"] = relationship(back_populates="product")

    def __str__(self):
        return self.name

class Service(Base):
    __tablename__ = 'service'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    third_party_id: Mapped[int] = mapped_column(ForeignKey("third_party.id"), index=True)
    type: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(512))    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    cost: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    third_party: Mapped["ThirdParty"] = relationship(back_populates="third_party")

    def __str__(self):
        return self.name
    
class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    third_party_id: Mapped[int] = mapped_column(ForeignKey("third_party.id"), index=True)
    category: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(512))    
    description: Mapped[str] = mapped_column(String(512))    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)    
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    third_party: Mapped["ThirdParty"] = relationship(back_populates="third_party")

    def __str__(self):
        return self.name    
    

class Sport(Base):
    __tablename__ = 'sport'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String(512))    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)    
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    events: Mapped["Event"] = relationship(back_populates="event")

    def __str__(self):
        return self.name  

class Event(Base):
    __tablename__ = 'event'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    third_party_id: Mapped[int] = mapped_column(ForeignKey("third_party.id"), index=True)
    city_id: Mapped[int] = mapped_column(Integer)
    sport_id: Mapped[int] = mapped_column(Integer)
    location: Mapped[str] = mapped_column(String(512))    
    event_date: Mapped[str] = mapped_column(DateTime)
    capacity: Mapped[int] = mapped_column(Integer)    
    description: Mapped[str] = mapped_column(String(512))    
    type: Mapped[str] = mapped_column(String(30))    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)    
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    third_party: Mapped["ThirdParty"] = relationship(back_populates="third_party")
    sport: Mapped["Sport"] = relationship(back_populates="sport")

    def __str__(self):
        return self.name        
         