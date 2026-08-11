from __future__ import annotations


def mock_conversion_resp():
    return {
        "id": "con_01FCTS1XMKH9FF43CAFA4CXT3P",
        "sell": {"amount": 1000, "currency": "GBP"},
        "buy": {
            "amount": 1247,
            "currency": "EUR",
            "fees": {
                "ryft": {"amount": 10},
                "platform": {"amount": 5, "ryftFee": {"amount": 2}},
            },
        },
        "rate": 1.247,
        "status": "Settled",
        "reason": "FX conversion",
        "estimatedSettlementDate": "2024-03-15",
        "settledTimestamp": 1470989600,
        "createdBy": {
            "id": "ac_b83f2653-06d7-44a9-a548-5825e8186004",
            "name": "Test Account",
        },
        "createdTimestamp": 1470989538,
    }


def mock_conversions_resp():
    return {
        "items": [mock_conversion_resp()],
    }


def mock_conversion_rate_resp():
    return {
        "sell": {"amount": 1000, "currency": "GBP"},
        "buy": {
            "amount": 1247,
            "currency": "EUR",
            "fees": {
                "ryft": {"amount": 10},
                "platform": {"amount": 5, "ryftFee": {"amount": 2}},
            },
        },
        "rate": 1.247,
        "estimatedSettlementDate": "2024-03-15",
    }
