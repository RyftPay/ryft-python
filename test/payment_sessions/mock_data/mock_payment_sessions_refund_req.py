from __future__ import annotations


def mock_refund_req_partial_refund():
    return {"amount": 250}


def mock_refund_req_with_reason():
    return {"amount": 250, "reason": "Returned by customer"}


def mock_refund_req_multi_capture_tx():
    return {
        "amount": 750,
        "captureTransaction": {
            "id": "txn_01FCTS1XMKH9FF43CAFA4CXT3P_01FCTS1XMKH9FF43CAFA4CXT3P"
        },
    }


def mock_refund_req_marketplace_refund_platform_fee():
    return {"amount": 250, "refundPlatformFee": True}


def mock_refund_req_marketplace_full_refund_split_payment():
    return {
        "splits": {
            "items": [
                {"id": "sp_01FCTS1XMKH9FF43CAFA4CXT3P"},
                {"id": "sp_01FCTS1XMKH9FF43CAFA4CXT4P"},
            ]
        }
    }


def mock_refund_req_marketplace_partial_refund_split_payment():
    return {
        "splits": {
            "items": [
                {"id": "sp_01FCTS1XMKH9FF43CAFA4CXT3P", "amount": 50},
                {
                    "id": "sp_01FCTS1XMKH9FF43CAFA4CXT4P",
                    "amount": 150,
                    "fee": {"amount": 50},
                },
            ]
        }
    }
