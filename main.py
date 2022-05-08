from fastapi import FastAPI

from app.routers import customers, invoices, plans, subscriptions
from app.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello micro billing application."}

app.include_router(customers.router, tags=['customers'])
app.include_router(invoices.router, tags=['invoices'])
app.include_router(plans.router, tags=['plans'])
app.include_router(subscriptions.router, tags=['subscriptions'])

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)
