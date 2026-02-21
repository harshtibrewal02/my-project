from fastapi import APIRouter
from fastapi.responses import JSONResponse
import time
import os
from app.config import settings

router = APIRouter()

START_TIME = time.time()


@router.get("/health")
def health_check() -> dict:
    # In demo mode, simulate a production failure
    # Set FORCE_HEALTH_FAIL=true in Render env to trigger rollback demo
    if os.getenv("FORCE_HEALTH_FAIL", "false").lower() == "true":
        raise RuntimeError("Simulated production failure for rollback demo")

    uptime_seconds = int(time.time() - START_TIME)
    minutes, seconds = divmod(uptime_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "uptime": f"{hours}h {minutes}m {seconds}s",
    }