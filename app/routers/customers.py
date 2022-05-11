from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.repositories import customer_repository
from app.database import session

router = APIRouter()


@router.get("/")
def get_customer_list(db: Session = Depends(session)):
    customers = customer_repository.list(db)
    return {"customers": [customer.to_dict() for customer in customers]}


@router.get("/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(session)):
    customer = customer_repository.get(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found.")
    return customer.to_dict()
