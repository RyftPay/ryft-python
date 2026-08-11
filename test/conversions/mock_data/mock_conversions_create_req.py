from __future__ import annotations


def mock_create_conversion_req():
    return {
        "sell": {"currency": "GBP", "amount": 1000},
        "buy": {"currency": "EUR"},
        "termAgreement": True,
        "reason": "FX conversion",
    }
