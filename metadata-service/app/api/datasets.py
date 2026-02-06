from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.schemas import DatasetCreate, DatasetResponse
from app.db.session import get_db
from app.models.dataset import Dataset, DatasetColumn

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.post("", response_model=DatasetResponse)
def create_dataset(payload: DatasetCreate, db: Session = Depends(get_db)):
    existing = db.query(Dataset).filter(Dataset.fqn == payload.fqn).first()
    if existing:
        raise HTTPException(status_code=400, detail="Dataset already exists")

    dataset = Dataset(
        fqn=payload.fqn,
        source_type=payload.source_type
    )

    for col in payload.columns:
        dataset.columns.append(
            DatasetColumn(name=col.name, type=col.type)
        )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset


@router.get("", response_model=list[DatasetResponse])
def list_datasets(db: Session = Depends(get_db)):
    return db.query(Dataset).all()
