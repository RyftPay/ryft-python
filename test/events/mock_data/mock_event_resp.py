def mock_event_resp():
    return {
        "id": "evt_123",
        "type": "PaymentSession.captured",
        "accountId": "acc_123",
        "createdTimestamp": 123456,
        "data": {
            "paymentSessionId": "pay_123",
            "amount": 123,
            "currency": "GBP",
            "status": "captured",
        },
    }


def mock_events_resp():
    return {"items": [mock_event_resp()]}
