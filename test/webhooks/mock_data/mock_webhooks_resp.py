def mock_webhook_created_resp():
    return {
        "secret": "whs_0f6b1b5a-aef0-4011-978b-19fd4a4d46ea",
        "id": "wh_31fba123-0fef-41d6-92ad-fd7089f49f8a",
        "active": True,
        "eventTypes": ["PaymentSession.captured", "PaymentSession.refunded"],
        "createdTimestamp": 1470989538,
    }


def mock_webhook_resp():
    return {
        "id": "wh_31fba123-0fef-41d6-92ad-fd7089f49f8a",
        "active": True,
        "eventTypes": ["PaymentSession.captured", "PaymentSession.refunded"],
        "createdTimestamp": 1470989538,
    }


def mock_webhooks_resp():
    return {
        "items": [mock_webhook_resp()],
    }
