import enum
import sqlalchemy as sa

from datetime import datetime
from sqlalchemy.orm import relationship

from .customer import Customer
from .plan import Plan
from ..database import Base


class SubscriptionStatusType(str, enum.Enum):
    active = "active"  # 有効
    past_due = "past_due"  # 遅延
    unpaid = "unpaid"  # 未払い
    canceled = "canceled"  # 解約
    incomplete = "incomplete"  # 不完全
    incomplete_expired = "incomplete_expired"  # 有効期限切れ
    trialing = "trialing"  # 試用


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = sa.Column(sa.Integer, primary_key=True)
    current_period_start = sa.Column(sa.DateTime, nullable=False)
    current_period_end = sa.Column(sa.DateTime, nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customers.id"), nullable=False)
    customer = relationship(Customer, backref="customers")
    plan_id = sa.Column(sa.Integer, sa.ForeignKey("plans.id"), nullable=False)
    plan = relationship(Plan, backref="plans")
    status = sa.Column(sa.Enum(SubscriptionStatusType), nullable=False)
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
