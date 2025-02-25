from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from .models import SessionLocal, PersonData
from sqlalchemy.sql.sqltypes import String
from datetime import datetime

router = APIRouter()

@router.get("/history")
def get_history(
    page: int = Query(1, alias="page", ge=1),
    limit: int = Query(10, alias="limit", ge=1, le=100),
    search_by_path: str = Query(None),
    min_people: int = Query(None, ge=0),
    max_people: int = Query(None, ge=0),
    start_time: str = Query(None),
    end_time: str = Query(None)
):
    """Fetches paginated history records with optional search and filtering."""
    db: Session = SessionLocal()

    query = db.query(PersonData)

    # Apply search filter on result image file path
    if search_by_path:
        query = query.filter(PersonData.result_image_file_path.like(f"%{search_by_path}%"))

    # Apply people count range filter
    if min_people is not None:
        query = query.filter(PersonData.num_bboxes >= min_people)
    if max_people is not None:
        query = query.filter(PersonData.num_bboxes <= max_people)

    # Apply time range filter
    if start_time:
        try:
            start_time_dt = datetime.fromisoformat(start_time)
            query = query.filter(PersonData.time >= start_time_dt)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid start_time format. Use ISO format: YYYY-MM-DDTHH:MM:SS")

    if end_time:
        try:
            end_time_dt = datetime.fromisoformat(end_time)
            query = query.filter(PersonData.time <= end_time_dt)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid end_time format. Use ISO format: YYYY-MM-DDTHH:MM:SS")

    # Pagination
    total_records = query.count()
    history_records = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "total": total_records,
        "page": page,
        "limit": limit,
        "records": history_records
    }
