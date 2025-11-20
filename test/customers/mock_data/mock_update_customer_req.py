from __future__ import annotations


def mock_update_customer_req():
    return {
        "firstName": "Jeff",
        "lastName": "Bridges",
        "homePhoneNumber": "+447900000000",
        "mobilePhoneNumber": "+447900000000",
        "metadata": {"customerId": "1", "registered": "123"},
        "defaultPaymentMethod": "pmt_01G0EYVFR02KBBVE2YWQ8AKMGJ",
    }
