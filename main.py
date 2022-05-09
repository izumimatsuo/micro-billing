from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import router


def get_app():
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title='Micro Billing', version='0.1.0')
    app.include_router(router, prefix="")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = get_app()
