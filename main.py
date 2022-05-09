from fastapi import FastAPI

from app.routers import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Micro Billing', version='0.1.0')
app.include_router(router, prefix="")

@app.get("/")
async def root():
    return {"message": "Hello micro billing application."}
