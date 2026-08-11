from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.plantation import PlantationCreate, PlantationResponse

router = APIRouter(
    prefix="/plantations",
    tags=["Plantations"],
)

plantations: list[PlantationResponse] = []


@router.post(
    "",
    response_model=PlantationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_plantation(data: PlantationCreate):
    plantation = PlantationResponse(
        id=uuid4(),
        **data.model_dump(),
        status="planted",
    )

    plantations.append(plantation)

    return plantation
