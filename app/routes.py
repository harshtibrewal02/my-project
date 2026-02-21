from fastapi import APIRouter
import time
from app.config import settings

router = APIRouter()

START_TIME = time.time()


@router.get("/health")
def health_check() -> dict:
    uptime_seconds = int(time.time() - START_TIME)
    minutes, seconds = divmod(uptime_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "uptime": f"{hours}h {minutes}m {seconds}s",
    }