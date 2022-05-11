from sqlalchemy.orm import Session

from app.models.customer import Customer


def list(db: Session):
    return db.query(Customer).all()


def get(db: Session, customer_id: int):
    return db.query(Customer).filter_by(id=customer_id).first()
