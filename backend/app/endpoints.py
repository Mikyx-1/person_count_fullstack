from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from .models import SessionLocal, PersonData
from sqlalchemy.sql.sqltypes import String

router = APIRouter()

@router.get("/history")
def get_history(
    page: int = Query(1, alias="page", ge=1),
    limit: int = Query(10, alias="limit", ge=1, le=100),
    search_by_path: str = Query(None),
    min_people: int = Query(None, ge=0),
    max_people: int = Query(None, ge=0)
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

    # Pagination
    total_records = query.count()
    history_records = query.offset((page - 1) * limit).limit(limit).all()

    # print(f"Total records found: {total_records}")  # Debugging

    return {
        "total": total_records,
        "page": page,
        "limit": limit,
        "records": history_records
    }
