from sqlalchemy.orm import Session

from app.models.invoice import Invoice


def list(db: Session):
    return db.query(Invoice).all()


def get(db: Session, invoice_id: int):
    return db.query(Invoice).filter_by(id=invoice_id).first()
