import sqlalchemy as sa

from datetime import datetime

from ..database import Base


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
