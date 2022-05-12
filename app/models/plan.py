import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum

from datetime import datetime

from .core import Currency
from ..database import Base


class Interval(str, enum.Enum):
    day = "day"
    week = "week"
    month = "month"
    year = "year"


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    currency = Column(Enum(Currency), nullable=False)
    interval = Column(Enum(Interval), nullable=False)
    interval_count = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            amount=self.amount,
            currency=self.currency,
            interval=self.interval,
            interval_count=self.interval_count,
        )
