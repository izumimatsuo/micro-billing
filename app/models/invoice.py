import enum
from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Session

from datetime import datetime

from .core import Currency
from ..database import Base


class InvoiceStatus(str, enum.Enum):
    draft = "draft"  # 未確定
    open = "open"  # 確定
    paid = "paid"  # 支払い済み
    void = "void"  # 請求謝り(キャンセル)
    uncollectible = "uncollectible"  # 回収不能


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    currency = Column(Enum(Currency), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    period_end = Column(DateTime, nullable=False)
    period_start = Column(DateTime, nullable=False)
    status = Column(Enum(InvoiceStatus), nullable=False)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=True)
    total = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def to_dict(self):
        return dict(
            id=self.id,
            currency=self.currency,
            customer_id=self.customer_id,
            period_end=str(self.period_end),
            period_start=str(self.period_start),
            status=self.status,
            subscription_id=self.subscription_id,
            total=self.total,
        )


def get_list(db: Session):
    return db.query(Invoice).all()


def get(db: Session, invoice_id: int):
    return db.query(Invoice).filter_by(id=invoice_id).first()
