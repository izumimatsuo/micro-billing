from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.repositories import subscription_repository, session


router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.get("/")
def get_subscription_list(db: Session = Depends(session)):
    subscriptions = subscription_repository.list(db)
    return {"subscriptions": [subscription.to_dict() for subscription in subscriptions]}


@router.get("/{subscription_id}")
def get_subscription(subscription_id: int, db: Session = Depends(session)):
    subscription = subscription_repository.get(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="subscription not found.")
    return subscription.to_dict()
