from fastapi import APIRouter

health_check_router = APIRouter(
    tags=["health check"]
)


@health_check_router.get("/")
async def health_check() -> str:
    return "pong"
