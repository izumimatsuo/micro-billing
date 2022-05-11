from app.database import SessionLocal


def session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
