import enum
import sqlalchemy as sa

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

    id = sa.Column(sa.Integer, primary_key=True)
    currency = sa.Column(sa.Enum(Currency), nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customers.id"), nullable=False)
    period_end = sa.Column(sa.DateTime, nullable=False)
    period_start = sa.Column(sa.DateTime, nullable=False)
    status = sa.Column(sa.Enum(InvoiceStatus), nullable=False)
    subscription_id = sa.Column(
        sa.Integer, sa.ForeignKey("subscriptions.id"), nullable=True
    )
    total = sa.Column(sa.Integer, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.now)
    updated_at = sa.Column(
        sa.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
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
