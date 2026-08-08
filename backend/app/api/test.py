from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def test_connection():
    return {
        "success": True,
        "message": "Frontend and backend are ready to communicate"
    }