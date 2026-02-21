from fastapi import FastAPI
from app.routes import router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(router, prefix="/api/v1")


@app.get("/")
def read_root() -> dict:
    return {
        "message": "API is running",
        "environment": settings.ENVIRONMENT
    }