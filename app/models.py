import enum
import sqlalchemy as sa

from datetime import datetime
from sqlalchemy.orm import relationship

from .database import Base


# ISO 4217
class Currency(str, enum.Enum):
    jpy = "jpy"
    usd = "usd"


class SubscriptionStatus(str, enum.Enum):
    active = "active"  # 有効
    past_due = "past_due"  # 遅延
    unpaid = "unpaid"  # 未払い
    canceled = "canceled"  # 解約
    incomplete = "incomplete"  # 不完全
    incomplete_expired = "incomplete_expired"  # 有効期限切れ
    trialing = "trialing"  # 試用


class InvoiceStatus(str, enum.Enum):
    draft = "draft"  # 未確定
    open = "open"  # 確定
    paid = "paid"  # 支払い済み
    void = "void"  # 請求謝り(キャンセル)
    uncollectible = "uncollectible"  # 回収不能


class Plan(Base):
    __tablename__ = "plans"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    amount = sa.Column(sa.Integer, nullable=False)
    currency = sa.Column(sa.Enum(Currency), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.now)
    updated_at = sa.Column(
        sa.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def __init__(self, id, name, amount, currency):
        self.id = id
        self.name = name
        self.amount = amount
        self.currency = currency

    def to_dict(self):
        return dict(
            id=self.id, name=self.name, amount=self.amount, currency=self.currency
        )


class Customer(Base):
    __tablename__ = "customers"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.now)
    updated_at = sa.Column(
        sa.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
        )


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = sa.Column(sa.Integer, primary_key=True)
    current_period_start = sa.Column(sa.DateTime, nullable=False)
    current_period_end = sa.Column(sa.DateTime, nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customers.id"), nullable=False)
    customer = relationship(Customer, backref="customers")
    plan_id = sa.Column(sa.Integer, sa.ForeignKey("plans.id"), nullable=False)
    plan = relationship(Plan, backref="plans")
    status = sa.Column(sa.Enum(SubscriptionStatus), nullable=False)
    start_date = sa.Column(sa.DateTime, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.now)
    updated_at = sa.Column(
        sa.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def __init__(
        self,
        id,
        current_period_start,
        current_period_end,
        customer_id,
        plan_id,
        status,
        start_date,
    ):
        self.id = id
        self.current_period_start = current_period_start
        self.current_period_end = current_period_end
        self.customer_id = customer_id
        self.plan_id = plan_id
        self.status = status
        self.start_date = start_date

    def to_dict(self):
        return dict(
            id=self.id,
            current_period_start=str(self.current_period_start),
            current_period_end=str(self.current_period_end),
            customer_id=self.customer_id,
            plan_id=self.plan_id,
            status=self.status,
            start_date=str(self.start_date),
        )


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

    def __init__(
        self,
        id,
        currency,
        customer_id,
        period_end,
        period_start,
        status,
        subscription_id,
        total,
    ):
        self.id = id
        self.currency = currency
        self.customer_id = customer_id
        self.period_end = period_end
        self.period_start = period_start
        self.status = status
        self.subscription_id = subscription_id
        self.total = total

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
