from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from datetime import datetime

from ..database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
        )


def get_list(db: Session):
    return db.query(Customer).all()


def get(db: Session, customer_id: int):
    return db.query(Customer).filter_by(id=customer_id).first()
