from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.lineage import DatasetLineage
from app.models.dataset import Dataset

router = APIRouter(prefix="/lineage", tags=["lineage"])


def creates_cycle(db: Session, upstream_id: int, downstream_id: int) -> bool:
    visited = set()

    def dfs(current_id):
        if current_id == upstream_id:
            return True
        visited.add(current_id)

        edges = db.query(DatasetLineage).filter(
            DatasetLineage.upstream_id == current_id
        ).all()

        for edge in edges:
            if edge.downstream_id not in visited:
                if dfs(edge.downstream_id):
                    return True
        return False

    return dfs(downstream_id)


@router.post("")
def add_lineage(upstream_fqn: str, downstream_fqn: str, db: Session = Depends(get_db)):
    upstream = db.query(Dataset).filter(Dataset.fqn == upstream_fqn).first()
    downstream = db.query(Dataset).filter(Dataset.fqn == downstream_fqn).first()

    if not upstream or not downstream:
        raise HTTPException(status_code=404, detail="Dataset not found")

    if creates_cycle(db, upstream.id, downstream.id):
        raise HTTPException(status_code=400, detail="Cycle detected. Lineage rejected.")

    lineage = DatasetLineage(
        upstream_id=upstream.id,
        downstream_id=downstream.id
    )

    db.add(lineage)
    db.commit()

    return {"message": "Lineage created successfully"}
