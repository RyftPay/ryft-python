from __future__ import annotations


def mock_create_customer_req():
    return {
        "email": "example@example.com",
        "firstName": "Jeff",
        "lastName": "Bridges",
        "homePhoneNumber": "+447900000000",
        "mobilePhoneNumber": "+447900000000",
        "metadata": {"customerId": "1", "registeredTimestamp": "123"},
    }
