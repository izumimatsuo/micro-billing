from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.repositories import plan_repository, session


router = APIRouter(prefix="/plans", tags=["plans"])


@router.get("/")
def get_plan_list(db: Session = Depends(session)):
    plans = plan_repository.list(db)
    return {"plans": [plan.to_dict() for plan in plans]}


@router.get("/{plan_id}")
def get_plan(plan_id: int, db: Session = Depends(session)):
    plan = plan_repository.get(db, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="plan not found.")
    return plan.to_dict()
