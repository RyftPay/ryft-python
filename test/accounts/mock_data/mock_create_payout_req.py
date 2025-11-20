from __future__ import annotations


def mock_create_payout_req():
    return {
        "amount": 5000,
        "currency": "GBP",
        "payoutMethodId": "pm_01FCTS1XMKH9FF43CAFA4CXT3P",
        "metadata": {"orderId": "1", "customerId": "123"},
    }
