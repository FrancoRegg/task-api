from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router

app = FastAPI(title="Task API")

app.include_router(health_router, prefix="/api/v1")
