from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.monitoring import MonitoringCreate, MonitoringResponse

router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"],
)

monitoring_records: list[MonitoringResponse] = []


@router.post(
    "",
    response_model=MonitoringResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_monitoring_record(data: MonitoringCreate):
    monitoring_record = MonitoringResponse(
        id=uuid4(),
        **data.model_dump(),
        status="recorded",
    )

    monitoring_records.append(monitoring_record)

    return monitoring_record
