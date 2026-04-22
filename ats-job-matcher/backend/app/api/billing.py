from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from app.services.payments import create_checkout_session

router = APIRouter(prefix="/billing", tags=["billing"])


class CheckoutRequest(BaseModel):
    email: EmailStr
    mode: str  # payment or subscription
    success_url: str
    cancel_url: str


class CheckoutResponse(BaseModel):
    checkout_url: str


@router.post("/checkout", response_model=CheckoutResponse)
def checkout(payload: CheckoutRequest) -> CheckoutResponse:
    url = create_checkout_session(
        customer_email=payload.email,
        mode=payload.mode,
        success_url=payload.success_url,
        cancel_url=payload.cancel_url,
    )
    return CheckoutResponse(checkout_url=url)
