def mock_payout_method_resp():
    return {
        "id": "pm_01G0EYVFR02KBBVE2YWQ8AKMGJ",
        "type": "BankAccount",
        "displayName": "string",
        "status": "Valid",
        "invalidReason": "string",
        "currency": "GBP",
        "countryCode": "GB",
        "bankAccount": {
            "bankIdType": "SortCode",
            "bankId": "string",
            "bankName": "string",
            "accountNumberType": "UnitedKingdom",
            "last4": "string",
            "address": {
                "lineOne": "string",
                "lineTwo": "string",
                "city": "string",
                "country": "GB",
                "postalCode": "string",
                "region": "string",
            },
        },
        "createdTimestamp": 1470989538,
        "lastUpdatedTimestamp": 1470989538,
    }


def mock_payout_methods_resp():
    return {"items": [mock_payout_method_resp()]}
