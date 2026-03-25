from fastapi import FastAPI
from app.config import settings
from app.routers import router as status_router
from app.db import engine, SessionLocal
from app import models, db

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)

app.include_router(status_router)

@app.get("/")
def root():
    return {"message": "API CRUD con FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
