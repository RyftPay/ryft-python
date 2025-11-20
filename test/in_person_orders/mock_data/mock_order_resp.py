from __future__ import annotations


def mock_in_person_order():
    return {
        "id": "ipord_01FCTS1XMKH9FF43CAFA4CXT3P",
        "status": "AwaitingPayment",
        "totalAmount": 6000,
        "taxAmount": 1000,
        "currency": "GBP",
        "items": [
            {
                "id": "ipsku_01FCTS1XMKH9FF43CAFA4CXT3P",
                "name": "Pax A920 Pro",
                "totalAmountPerUnit": 6000,
                "taxAmountPerUnit": 1000,
                "quantity": 1,
            }
        ],
        "shipping": None,
        "tracking": None,
        "metadata": {"orderId": "123"},
        "createdTimestamp": 1470989538,
        "lastUpdatedTimestamp": 1470989538,
    }


def mock_in_person_orders():
    return {
        "items": [mock_in_person_order()],
        "paginationToken": None,
    }
