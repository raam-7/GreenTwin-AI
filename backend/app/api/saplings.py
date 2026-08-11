from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.sapling import SaplingCreate, SaplingResponse

router = APIRouter(
    prefix="/saplings",
    tags=["Saplings"],
)

saplings: list[SaplingResponse] = []


@router.post(
    "",
    response_model=SaplingResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_sapling(data: SaplingCreate):
    sapling = SaplingResponse(
        id=uuid4(),
        **data.model_dump(),
        grade=None,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    saplings.append(sapling)

    return sapling


@router.get("", response_model=list[SaplingResponse])
def get_saplings():
    return saplings
