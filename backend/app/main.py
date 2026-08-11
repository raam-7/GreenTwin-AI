from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ai import router as ai_router
from app.api.monitoring import router as monitoring_router
from app.api.test import router as test_router
from app.api.nurseries import router as nursery_router
from app.api.plantations import router as plantation_router
from app.api.saplings import router as sapling_router

app = FastAPI(
    title="GreenTwin AI API",
    description="AI-powered afforestation monitoring and decision support platform",
    version="0.1.0",
)

app.include_router(nursery_router, prefix="/api")
app.include_router(sapling_router, prefix="/api")
app.include_router(plantation_router, prefix="/api")
app.include_router(monitoring_router, prefix="/api")
app.include_router(ai_router, prefix="/api/ai")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "GreenTwin AI API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
