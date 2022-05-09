from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories import SubscriptionRepository
from ..database import session

router = APIRouter()


@router.get("/")
def get_subscription_list(db: Session = Depends(session)):
    subscriptions = SubscriptionRepository.list(db)
    return {"subscriptions": [subscription.to_dict() for subscription in subscriptions]}


@router.get("/{subscription_id}")
def get_subscription(subscription_id: int, db: Session = Depends(session)):
    subscription = SubscriptionRepository.get(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="subscription not found.")
    return subscription.to_dict()
