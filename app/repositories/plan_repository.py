from sqlalchemy.orm import Session

from app.models.plan import Plan


def list(db: Session):
    return db.query(Plan).all()


def get(db: Session, plan_id: int):
    return db.query(Plan).filter_by(id=plan_id).first()
