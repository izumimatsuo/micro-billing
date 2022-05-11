from sqlalchemy.orm import Session

from app.models.subscription import Subscription


def list(db: Session):
    return db.query(Subscription).all()


def get(db: Session, subscription_id: int):
    return db.query(Subscription).filter_by(id=subscription_id).first()
