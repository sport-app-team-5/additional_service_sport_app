import logging
from fastapi import FastAPI, APIRouter
from app import api
from config import settings


app = FastAPI()
app.title = settings.PROJECT_NAME
app.version = settings.PROJECT_VERSION

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

api_v1_auth = APIRouter(prefix='/api/v1/auth')
api_v1_auth.include_router(api.additional_services_router)
app.include_router(api.health_check_router)
app.include_router(api_v1_auth)

app_test = app
