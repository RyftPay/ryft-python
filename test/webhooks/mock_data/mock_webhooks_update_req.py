from __future__ import annotations


def mock_update_webhook_req():
    return {
        "url": "https://example-endpoint.com/webhook",
        "active": True,
        "eventTypes": ["PaymentSession.captured", "PaymentSession.refunded"],
    }
