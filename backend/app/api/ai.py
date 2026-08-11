from typing import Literal
from uuid import UUID

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

router = APIRouter(tags=["AI"])


class GradeResponse(BaseModel):
    sapling_id: UUID
    grade: Literal["A", "B", "C"]
    confidence: float


class HealthResponse(BaseModel):
    sapling_id: UUID
    monitoring_id: UUID
    status: Literal["Healthy", "Stressed", "Dead"]
    confidence: float


def validate_image_file(image: UploadFile) -> None:
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must be an image",
        )


@router.post("/grade", response_model=GradeResponse)
def grade_sapling(
    sapling_id: UUID = Form(...),
    image: UploadFile = File(...),
):
    validate_image_file(image)

    return GradeResponse(
        sapling_id=sapling_id,
        grade="A",
        confidence=0.94,
    )


@router.post("/health", response_model=HealthResponse)
def predict_health(
    sapling_id: UUID = Form(...),
    monitoring_id: UUID = Form(...),
    image: UploadFile = File(...),
):
    validate_image_file(image)

    return HealthResponse(
        sapling_id=sapling_id,
        monitoring_id=monitoring_id,
        status="Healthy",
        confidence=0.91,
    )
