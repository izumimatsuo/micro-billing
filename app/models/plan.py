import enum
import sqlalchemy as sa

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

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    amount = sa.Column(sa.Integer, nullable=False)
    currency = sa.Column(sa.Enum(Currency), nullable=False)
    interval = sa.Column(sa.Enum(Interval), nullable=False)
    interval_count = sa.Column(sa.Integer, nullable=False, default=1)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.now)
    updated_at = sa.Column(
        sa.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
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
