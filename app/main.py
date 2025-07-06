from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(title="Task API")

app.include_router(health_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
