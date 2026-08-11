from uuid import UUID

from pydantic import BaseModel, Field


class SaplingCreate(BaseModel):
    nursery_id: UUID
    species: str = Field(min_length=1)
    source: str = Field(min_length=1)
    image_url: str = Field(min_length=1)


class SaplingResponse(BaseModel):
    id: UUID
    nursery_id: UUID
    species: str
    source: str
    image_url: str
    grade: str | None = None
    created_at: str
