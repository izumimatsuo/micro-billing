from fastapi import APIRouter
from app.routers import customers, invoices, plans, subscriptions


router = APIRouter()
router.include_router(customers.router)
router.include_router(invoices.router)
router.include_router(plans.router)
router.include_router(subscriptions.router)
