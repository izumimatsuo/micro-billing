import sqlalchemy as sa

from datetime import datetime

from .core import Currency
from ..database import Base


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
