from __future__ import annotations


def mock_in_person_product():
    return {
        "id": "ippd_01FCTS1XMKH9FF43CAFA4CXT3P",
        "name": "PAX A920 Pro",
        "status": "Available",
        "description": "A professional payment terminal",
        "details": {
            "battery": "5150mAh | 3.7V",
            "cardReaders": "Chip & PIN | Contactless | Magnetic Stripe",
        },
        "createdTimestamp": 1470989538,
        "lastUpdatedTimestamp": 1470989538,
    }


def mock_in_person_products():
    return {
        "items": [mock_in_person_product()],
        "paginationToken": None,
    }
