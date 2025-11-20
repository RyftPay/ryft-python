def mock_terminal():
    return {
        "id": "tml_01FCTS1XMKH9FF43CAFA4CXT3P",
        "name": "Front of house",
        "location": {"id": "iploc_01FCTS1XMKH9FF43CAFA4CXT3P"},
        "device": {"type": "PAX A920 Pro", "serialNumber": "1234567890"},
        "action": None,
        "metadata": {"internalID": "1"},
        "createdTimestamp": 1470989538,
        "lastUpdatedTimestamp": 1470989538,
    }


def mock_terminals():
    return {
        "items": [mock_terminal()],
        "paginationToken": None,
    }


def mock_create_terminal_req():
    return {
        "serialNumber": "1234567890",
        "name": "Front of house",
        "locationId": "iploc_01FCTS1XMKH9FF43CAFA4CXT3P",
        "metadata": {"internalID": "1"},
    }


def mock_update_terminal_req():
    return {
        "name": "Updated Terminal Name",
        "metadata": {"updated": "true"},
    }


def mock_payment_req():
    return {
        "amounts": {"requested": 1000},
        "currency": "GBP",
        "paymentSession": {"platformFee": 50},
    }


def mock_refund_req():
    return {
        "paymentSession": {"id": "ps_01FCTS1XMKH9FF43CAFA4CXT3P"},
        "amount": 1000,
        "refundPlatformFee": False,
    }


def mock_confirm_receipt_req():
    return {
        "customerCopy": {"status": "Succeeded"},
        "merchantCopy": {"status": "Succeeded"},
    }
