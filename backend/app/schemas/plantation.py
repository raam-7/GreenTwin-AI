from uuid import UUID

from pydantic import BaseModel, Field


class PlantationCreate(BaseModel):
    sapling_id: UUID
    plantation_date: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    site_id: UUID


class PlantationResponse(BaseModel):
    id: UUID
    sapling_id: UUID
    plantation_date: str
    latitude: float
    longitude: float
    site_id: UUID
    status: str
