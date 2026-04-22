from __future__ import annotations

import stripe

from app.core.config import settings

stripe.api_key = settings.stripe_secret_key


def create_checkout_session(customer_email: str, mode: str, success_url: str, cancel_url: str) -> str:
    """
    mode: 'payment' for pay-as-you-go, 'subscription' for pro monthly.
    """
    price = settings.stripe_price_payg if mode == "payment" else settings.stripe_price_pro_monthly
    session = stripe.checkout.Session.create(
        mode=mode,
        customer_email=customer_email,
        line_items=[{"price": price, "quantity": 1}],
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session.url
