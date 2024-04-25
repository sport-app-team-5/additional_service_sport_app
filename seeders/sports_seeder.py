from typing import List
from sqlalchemy.orm import Session

from app.modules.services.domain.entities import Sport



def sports_seeder(db: Session):
    sports_to_create = [
        Sport(name="Ciclismo", code="CI"),
        Sport(name="Atletismo", code="AT")
    ]
    create_or_update(db, sports_to_create)
    db.commit()


def create_or_update(db: Session, sports: List[Sport]):
    for sport in sports:
        sport_db = db.query(Sport).filter_by(name=sport.name).first()

        if sport_db:
            sport_db.code = sport.code
            sport_db.name = sport.name
        else:
            db.add(sport)