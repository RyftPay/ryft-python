def mock_customer_resp():
    return {
        "email": "example@example.com",
        "firstName": "Jeff",
        "lastName": "Bridges",
        "homePhoneNumber": "+447900000000",
        "mobilePhoneNumber": "+447900000000",
        "metadata": {"customerId": "1", "registeredTimestamp": "123"},
    }


def mock_customers_resp():
    return {
        "items": [mock_customer_resp()],
    }
