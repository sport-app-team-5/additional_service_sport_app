import logging
from fastapi import FastAPI
from app.config.api import app_configs
from app.api.v1.router import private_router as private_v1
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = FastAPI(**app_configs)
app.add_middleware(CORSMiddleware, allow_origins='*', allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(private_v1, prefix="/api/v1")
