from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.nursery import NurseryCreate, NurseryResponse

router = APIRouter(
    prefix="/nurseries",
    tags=["Nurseries"],
)

nurseries: list[NurseryResponse] = []


@router.post(
    "",
    response_model=NurseryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_nursery(data: NurseryCreate):
    nursery = NurseryResponse(
        id=uuid4(),
        **data.model_dump(),
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    nurseries.append(nursery)

    return nursery


@router.get("", response_model=list[NurseryResponse])
def get_nurseries():
    return nurseries