import csv
import calendar
from io import StringIO
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy import extract

from app.models.subscription import Subscription, SubscriptionStatus
from app.repositories import invoice_repository, session


router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.get("/")
def get_invoice_list(db: Session = Depends(session)):
    invoices = invoice_repository.list(db)
    return {"invoices": [invoice.to_dict() for invoice in invoices]}


@router.get("/data")
def create_invoices(db: Session = Depends(session)):
    f = StringIO()
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    writer.writerow(["name", "amount", "start_date"])
    for t in (
        db.query(Subscription)
        .filter(Subscription.status == SubscriptionStatus.active)
        .all()
    ):
        writer.writerow([t.customer.name, t.plan.amount, t.start_date])

    #    'Content-Disposition': 'attachment; filename='+ obj +'.csv'
    return Response(content=f.getvalue(), media_type="text/csv")


@router.get("/{invoice_id}")
def get_invoice(invoice_id: int, db: Session = Depends(session)):
    invoice = invoice_repository.get(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="invoice not found.")
    return invoice.to_dict()


@router.get("/data/{invoice_date}")
def create_invoices_by_date(invoice_date: str, db: Session = Depends(session)):

    try:
        invoice_datetime = datetime.strptime(invoice_date, "%Y%m%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="bad request.")

    if (
        invoice_datetime.day
        == calendar.monthrange(invoice_datetime.year, invoice_datetime.month)[1]
    ):
        targets = (
            db.query(Subscription)
            .filter(
                Subscription.status == SubscriptionStatus.active,
                extract("day", Subscription.start_date) >= invoice_datetime.day,
            )
            .all()
        )
    else:
        targets = (
            db.query(Subscription)
            .filter(
                Subscription.status == SubscriptionStatus.active,
                extract("day", Subscription.start_date) == invoice_datetime.day,
            )
            .all()
        )

    f = StringIO()
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    writer.writerow(["name", "amount", "start_date"])
    for t in targets:
        writer.writerow([t.customer.name, t.plan.amount, t.start_date])

    #    'Content-Disposition': 'attachment; filename='+ obj +'.csv'
    return Response(content=f.getvalue(), media_type="text/csv")
