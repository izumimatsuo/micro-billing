from sqlalchemy.orm import Session

from .models.customer import Customer

class CustomerRepository:
    @staticmethod
    def list(db: Session):
        return db.query(Customer).all()

    @staticmethod
    def get(db: Session, customer_id: int):
        return db.query(Customer).filter_by(id=customer_id).first()


from .models.plan import Plan

class PlanRepository:
    @staticmethod
    def list(db: Session):
        return db.query(Plan).all()

    @staticmethod
    def get(db: Session, plan_id: int):
        return db.query(Plan).filter_by(id=plan_id).first()


from .models.subscription import Subscription

class SubscriptionRepository:
    @staticmethod
    def list(db: Session):
        return db.query(Subscription).all()

    @staticmethod
    def get(db: Session, subscription_id: int):
        return db.query(Subscription).filter_by(id=subscription_id).first()


from .models.invoice import Invoice

class InvoiceRepository:
    @staticmethod
    def list(db: Session):
        return db.query(Invoice).all()

    @staticmethod
    def get(db: Session, invoice_id: int):
        return db.query(Invoice).filter_by(id=invoice_id).first()
