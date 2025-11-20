from __future__ import annotations


def mock_update_payout_method_req():
    return {
        "displayName": "string",
        "bankAccount": {
            "bankIdType": "SortCode",
            "bankId": "string",
            "accountNumberType": "UnitedKingdom",
            "accountNumber": "string",
            "address": {
                "lineOne": "string",
                "lineTwo": "string",
                "city": "string",
                "country": "GB",
                "postalCode": "string",
                "region": "string",
            },
        },
    }
