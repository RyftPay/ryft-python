def mock_create_payout_method_req_gbp_bank_acc():
    return {
        "type": "BankAccount",
        "currency": "GBP",
        "countryCode": "GB",
        "bankAccount": {
            "bankIdType": "SortCode",
            "bankId": "123456",
            "accountNumberType": "UnitedKingdom",
            "accountNumber": "12345678",
            "address": {
                "lineOne": "123 Street",
                "city": "Manchester",
                "country": "GB",
                "postalCode": "M1 1AA",
            },
        },
    }


def mock_create_payout_method_req_eur_bank_acc():
    return {
        "type": "BankAccount",
        "currency": "EUR",
        "countryCode": "IE",
        "bankAccount": {
            "accountNumberType": "Iban",
            "accountNumber": "IE64IRCE92050112345678",
            "address": {
                "lineOne": "123 Street",
                "city": "Dublin",
                "country": "IE",
                "postalCode": "DO1 1AA",
            },
        },
    }


def mock_create_payout_method_req_us_bank_acc():
    return {
        "type": "BankAccount",
        "currency": "USD",
        "countryCode": "US",
        "bankAccount": {
            "bankIdType": "RoutingNumber",
            "bankId": "026014928",
            "accountNumberType": "UnitedStates",
            "accountNumber": "253368194864",
            "address": {
                "lineOne": "123 Street",
                "city": "Beverly Hills",
                "country": "US",
                "postalCode": "90210",
                "region": "CA",
            },
        },
    }
