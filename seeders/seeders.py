from sqlalchemy.orm import Session
from . import sports_seeder

def all_seeders(db: Session):
    sports_seeder(db)