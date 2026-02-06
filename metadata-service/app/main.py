from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.datasets import router as dataset_router
from app.api.search import router as search_router
from app.api.lineage import router as lineage_router

app = FastAPI(title="Metadata Service")

app.include_router(dataset_router)
app.include_router(search_router)
app.include_router(lineage_router)

@app.get("/")
def health_check():
    return {"status": "api running"}

