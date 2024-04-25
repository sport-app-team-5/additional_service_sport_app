from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.config.db import get_db
from app.config.env import env
from app.seedwork.presentation.jwt import oauth2_scheme
from seeders.seeders import all_seeders
from sqlalchemy.orm import Session

seeder_router = APIRouter(
    prefix='/seeders',
    tags=["Seeders"],
    dependencies=[Depends(oauth2_scheme)]
)


@seeder_router.post("", status_code=status.HTTP_201_CREATED)
async def run_seeders(password: str = Query(..., min_length=3), db: Session = Depends(get_db)) -> dict:
    if password == env.SECRET_KEY:
        all_seeders(db)
        return {"message": "Seeders created"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')
