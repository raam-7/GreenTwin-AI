from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class MonitoringCreate(BaseModel):
    plantation_id: UUID
    sapling_id: UUID
    observed_at: datetime
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    image_url: str = Field(min_length=1)
    notes: str = Field(min_length=1)


class MonitoringResponse(BaseModel):
    id: UUID
    plantation_id: UUID
    sapling_id: UUID
    observed_at: datetime
    latitude: float
    longitude: float
    image_url: str
    notes: str
    status: str
