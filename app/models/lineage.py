from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base

class DatasetLineage(Base):
    __tablename__ = "dataset_lineage"

    id = Column(Integer, primary_key=True, index=True)
    upstream_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    downstream_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
