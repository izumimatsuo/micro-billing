from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories import PlanRepository
from ..database import session

router = APIRouter()


@router.get("/plans/")
def get_plan_list(db: Session = Depends(session)):
    plans = PlanRepository.list(db)
    return {"plans": [plan.to_dict() for plan in plans]}


@router.get("/plans/{plan_id}")
def get_plan(plan_id: int, db: Session = Depends(session)):
    plan = PlanRepository.get(db, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="plan not found.")
    return plan.to_dict()
