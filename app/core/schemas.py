from pydantic import BaseModel, validator
from typing import List


# ---------- REQUEST SCHEMAS ----------

class ColumnCreate(BaseModel):
    name: str
    type: str


class DatasetCreate(BaseModel):
    fqn: str
    source_type: str
    columns: List[ColumnCreate]

    @validator("fqn")
    def validate_fqn(cls, v):
        parts = v.split(".")
        if len(parts) != 4:
            raise ValueError(
                "FQN must be in the format: connection.database.schema.table"
            )
        return v

    @validator("columns")
    def validate_columns(cls, v):
        if not v:
            raise ValueError("Dataset must have at least one column")

        names = [col.name for col in v]
        if len(names) != len(set(names)):
            raise ValueError("Duplicate column names are not allowed")

        return v

    @validator("source_type")
    def validate_source_type(cls, v):
        allowed = {"mysql", "postgres", "snowflake"}
        if v.lower() not in allowed:
            raise ValueError(
                f"source_type must be one of {allowed}"
            )
        return v.lower()


# ---------- RESPONSE SCHEMAS ----------

class ColumnResponse(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True


class DatasetResponse(BaseModel):
    fqn: str
    source_type: str
    columns: List[ColumnResponse]

    class Config:
        orm_mode = True
