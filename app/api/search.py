from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.db.session import get_db
from app.models.dataset import Dataset, DatasetColumn
from app.core.schemas import DatasetResponse

router = APIRouter(tags=["search"])

@router.get("/search", response_model=list[DatasetResponse])
def search_datasets(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    datasets = (
        db.query(Dataset)
        .outerjoin(DatasetColumn)
        .filter(
            or_(
                Dataset.fqn.ilike(f"%{q}%"),
                DatasetColumn.name.ilike(f"%{q}%")
            )
        )
        .distinct()
        .all()
    )
    return datasets
