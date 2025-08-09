def mock_create_webhook_req():
    return {
        "url": "https://example-endpoint.com/webhook",
        "active": True,
        "eventTypes": ["PaymentSession.captured", "PaymentSession.refunded"],
    }
