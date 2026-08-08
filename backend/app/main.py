from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.test import router as test_router

app = FastAPI(
    title="GreenTwin AI API",
    description="AI-powered afforestation monitoring and decision support platform",
    version="0.1.0",
)

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