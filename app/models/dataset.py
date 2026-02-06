from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    fqn = Column(String(255), unique=True, index=True, nullable=False)
    source_type = Column(String(50), nullable=False)

    columns = relationship("DatasetColumn", back_populates="dataset", cascade="all, delete")


class DatasetColumn(Base):
    __tablename__ = "dataset_columns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)

    dataset_id = Column(Integer, ForeignKey("datasets.id"))
    dataset = relationship("Dataset", back_populates="columns")
