from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import Float, String, DateTime, Boolean, ForeignKey, Integer
from app.config.db import Base

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
        return self.name