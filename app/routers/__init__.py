from fastapi import APIRouter
from app.routers import customers, invoices, plans, subscriptions


router = APIRouter()
router.include_router(customers.router, prefix="/customers", tags=["customers"])
router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
router.include_router(plans.router, prefix="/plans", tags=["plans"])
router.include_router(
    subscriptions.router, prefix="/subscriptions", tags=["subscriptions"]
)
