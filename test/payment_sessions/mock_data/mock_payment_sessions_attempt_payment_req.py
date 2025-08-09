def mock_attempt_payment_req_with_card():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "cardDetails": {
            "number": "4444333322221111",
            "expiryMonth": "10",
            "expiryYear": "2024",
            "cvc": "100",
        },
    }


def mock_attempt_payment_req_with_card_and_save():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "cardDetails": {
            "number": "4444333322221111",
            "expiryMonth": "10",
            "expiryYear": "2024",
            "cvc": "100",
        },
        "paymentMethodOptions": {"store": True},
    }


def mock_attempt_payment_req_with_saved_payment_method():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "paymentMethod": {"id": "pmt_01G0EYVFR02KBBVE2YWQ8AKMGJ"},
    }


def mock_attempt_payment_req_with_google_pay_token():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "walletDetails": {
            "type": "GooglePay",
            "googlePayToken": '{"signature":"MEYCIQCOjFuUGDkyieeJCQkm23qMSsQtGRjjVcWuAEHjdcGtNH+fx9GD342jNa","intermediateSigningKey":{"signedKey":"{\\"keyValue\\":\\"MFkwEjHIVnhmXEs2OjgvsLYCuiwXttkLpM5EFA3snvzPBUzT9hFeUuPCBTyP+83vbpNo5WFqjObGuVj3EFYRa0bGQ0+4ZYlk16tk4cGqVliuD2VS+ooPiDzztKahTj3tNicjyUjpD7AxiMPf/RHsHTlXs+m79EibjQxyE/CjlqrwfA3qpxJpdkt/ihS8JlVhQP8d/gnV/Get36o02gZc/F9s7kfG6Ur/rZ0Nf5F0yVCfZfgYCIeEPE415sjm0yJehlmVJ+iWrsdoUjrTlDfNqUj8m44vfxyrmTbk2HaAgy+LWyu0DtBFHtQsecZpGyYLGbiTRbL/F6wXEZEcM9W8lFy7pNtyx2FpvGFKPOnM8hAEhJ6OkDHMNmBSZWoqY9PLeVeXvbuW9KdKzHeGkFQmsypKBrkT5XDmP49AFAnaGyVfvtBunLdt4SrPqJgSpvLdBhvOwHNQRSAaaUx6xBQqEecVAZF/fdwpcMXc2Mc\\",\\"ephemeralPublicKey\\":\\"BEPsTEoiu6nyicBC9EhvTE45t8+IxjiKiifT/tmytIhn+O6d+cGSuiSmzeg1k1X0xZqr...",\\"tag\\":\\"pDKKl7MBNL+CnyrY6XB8E/T6hbbnEo8q4\\\\u003d\\"}"}',
        },
    }


def mock_attempt_payment_req_with_apple_pay_token():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "walletDetails": {
            "type": "ApplePay",
            "applePayToken": "eyJ2ZXJzaW9uIjoiRUNfdjEiLCJkYXRhIjoiN21Fay9BSGh2OXJzSmM1K0NFbVhRaERHaHZCMjViaDFxb0hTZmVVWHpiNFA5Nk5ieWd6alV3ZnR3RXJUYmRhQ3FFMXFi......",
        },
    }


def mock_attempt_payment_req_with_billing_address_included():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "cardDetails": {
            "number": "4444333322221111",
            "expiryMonth": "10",
            "expiryYear": "2024",
            "cvc": "100",
        },
        "billingAddress": {
            "firstName": "Fox",
            "lastName": "Mulder",
            "lineOne": "Stonehenge",
            "postalCode": "SP4 7DE",
            "city": "Salisbury",
            "country": "GB",
        },
    }


def mock_attempt_payment_req_with_customer_included():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "cardDetails": {
            "number": "4444333322221111",
            "expiryMonth": "10",
            "expiryYear": "2024",
            "cvc": "100",
        },
        "customerDetails": {"email": "example@mail.com"},
    }


def mock_attempt_payment_req_with_3ds():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "cardDetails": {
            "number": "4444333322221111",
            "expiryMonth": "10",
            "expiryYear": "2024",
            "cvc": "100",
        },
        "threeDsRequestDetails": {
            "deviceChannel": "Browser",
            "browserDetails": {
                "acceptHeader": "application/json,text/plain,text/html,*/*",
                "colorDepth": 24,
                "javaEnabled": True,
                "language": "en-GB",
                "screenHeight": 900,
                "screenWidth": 1440,
                "timeZoneOffset": -120,
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            },
        },
    }
