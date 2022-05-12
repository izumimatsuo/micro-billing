import enum
from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey

from datetime import datetime
from sqlalchemy.orm import relationship

from .customer import Customer
from .plan import Plan
from ..database import Base


class SubscriptionStatus(str, enum.Enum):
    active = "active"  # 有効
    past_due = "past_due"  # 遅延
    unpaid = "unpaid"  # 未払い
    canceled = "canceled"  # 解約
    incomplete = "incomplete"  # 不完全
    incomplete_expired = "incomplete_expired"  # 有効期限切れ
    trialing = "trialing"  # 試用


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    current_period_start = Column(DateTime, nullable=False)
    current_period_end = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer = relationship(Customer, backref="customers")
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    plan = relationship(Plan, backref="plans")
    status = Column(Enum(SubscriptionStatus), nullable=False)
    start_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

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
