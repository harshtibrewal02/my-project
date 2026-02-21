from fastapi import APIRouter
from fastapi.responses import JSONResponse
import time
from app.config import settings

router = APIRouter()

START_TIME = time.time()


@router.get("/health")
def health_check() -> JSONResponse:
    # 💥 INTENTIONAL BUG FOR ROLLBACK DEMO
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Simulated failure for demo"}
    )