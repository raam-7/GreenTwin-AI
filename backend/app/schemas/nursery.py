from pydantic import BaseModel, Field
from uuid import UUID


class NurseryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    location: str = Field(min_length=2, max_length=255)
    latitude: float
    longitude: float
    manager_name: str = Field(min_length=2, max_length=150)
    capacity: int = Field(gt=0)


class NurseryResponse(NurseryCreate):
    id: UUID
    created_at: str