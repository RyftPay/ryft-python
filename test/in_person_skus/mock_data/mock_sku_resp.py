def mock_in_person_sku():
    return {
        "id": "ipsku_01FCTS1XMKH9FF43CAFA4CXT3P",
        "name": "PAX A920 Pro",
        "country": "GB",
        "totalAmount": 5000,
        "currency": "GBP",
        "status": "Available",
        "productId": "ippd_01FCTS1XMKH9FF43CAFA4CXT3P",
        "createdTimestamp": 1470989538,
        "lastUpdatedTimestamp": 1470989538,
    }


def mock_in_person_skus():
    return {
        "items": [mock_in_person_sku()],
        "paginationToken": None,
    }
