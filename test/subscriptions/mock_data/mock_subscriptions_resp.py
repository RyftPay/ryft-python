def mock_payment_sessions_resp():
    return {
        "items": [
            {
                "id": "ps_01FCTS1XMKH9FF43CAFA4CXT3P",
                "amount": 500,
                "currency": "GBP",
                "paymentType": "Standard",
                "entryMode": "Online",
                "customerEmail": "example@mail.com",
                "customerDetails": {
                    "id": "cus_01G0EYVFR02KBBVE2YWQ8AKMGJ",
                    "firstName": "Fred",
                    "lastName": "Jones",
                    "homePhoneNumber": "+447900000000",
                    "mobilePhoneNumber": "+447900000000",
                    "metadata": {"customerId": "123"},
                },
                "credentialOnFileUsage": {
                    "initiator": "Customer",
                    "sequence": "Initial",
                },
                "previousPayment": {"id": "string"},
                "rebillingDetail": {
                    "amountVariance": "Fixed",
                    "numberOfDaysBetweenPayments": 30,
                    "totalNumberOfPayments": 12,
                    "currentPaymentNumber": 1,
                    "expiry": 1776988800,
                },
                "enabledPaymentMethods": ["Card"],
                "paymentMethod": {
                    "type": "Card",
                    "tokenizedDetails": {
                        "id": "pmt_01G0EYVFR02KBBVE2YWQ8AKMGJ",
                        "stored": True,
                    },
                    "card": {"scheme": "Mastercard", "last4": "4242"},
                    "wallet": {"type": "GooglePay"},
                    "billingAddress": {
                        "firstName": "string",
                        "lastName": "string",
                        "lineOne": "string",
                        "lineTwo": "string",
                        "city": "string",
                        "country": "GB",
                        "postalCode": "string",
                        "region": "string",
                    },
                    "checks": {"avsResponseCode": "Y", "cvvResponseCode": "M"},
                },
                "platformFee": 50,
                "splitPaymentDetail": {
                    "items": [
                        {
                            "id": "sp_01FCTS1XMKH9FF43CAFA4CXT3P",
                            "accountId": "ac_b83f2653-06d7-44a9-a548-5825e8186004",
                            "amount": 50,
                            "fee": {"amount": 50},
                            "description": "2 x The Selfish Gene",
                            "metadata": {
                                "productId": "123",
                                "productDescription": "The Selfish Gene",
                            },
                        }
                    ]
                },
                "status": "PendingPayment",
                "metadata": {"orderNumber": "123"},
                "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
                "lastError": "insufficient_funds",
                "refundedAmount": 120,
                "statementDescriptor": {"descriptor": "Ryft Ltd", "city": "London"},
                "requiredAction": {
                    "type": "Redirect",
                    "url": "https://ryftpay.com/3ds-auth",
                },
                "returnUrl": "https://ryftpay.com/checkout?orderId=123&ps=ps_01FCTS1XMKH9FF43CAFA4CXT3P",
                "authorizationType": "FinalAuth",
                "captureFlow": "Automatic",
                "verifyAccount": True,
                "shippingDetails": {
                    "address": {
                        "firstName": "Fox",
                        "lastName": "Mulder",
                        "lineOne": "Stonehenge",
                        "postalCode": "SP4 7DE",
                        "city": "Salisbury",
                        "country": "GB",
                    }
                },
                "orderDetails": {
                    "items": [
                        {
                            "reference": "product123",
                            "name": "The Big Gundown (Blu-ray)",
                            "quantity": 2,
                            "unitPrice": 250,
                            "taxAmount": 50,
                            "totalAmount": 540,
                            "discountAmount": 10,
                            "productUrl": "string",
                            "imageUrl": "string",
                        }
                    ]
                },
                "paymentSettings": {"paymentMethodOptions": {"disabled": ["Amex"]}},
                "createdTimestamp": 1470989538,
            }
        ],
        "paginationToken": "ps_01FCTS1XMKH9FF43CAFA4CXT3P",
    }


def mock_subscription_resp():
    return {
        "id": "sub_01G0EYVFR02KBBVE2YWQ8AKMGJ",
        "status": "Pending",
        "description": "Bob's monthly gym membership",
        "customer": {"id": "cus_01G0EYVFR02KBBVE2YWQ8AKMGJ"},
        "paymentMethod": {"id": "pmt_01G0EYVFR02KBBVE2YWQ8AKMGJ"},
        "paymentSessions": {
            "initial": {
                "id": "ps_01G0EYVFR02KBBVE2YWQ8AKMGJ",
                "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
                "requiredAction": {
                    "type": "Redirect",
                    "url": "https://ryftpay.com/3ds-auth",
                },
            },
            "latest": {
                "id": "ps_01G0EYVFR02KBBVE2YWQ8AKMGJ",
                "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
                "requiredAction": {
                    "type": "Redirect",
                    "url": "https://ryftpay.com/3ds-auth",
                },
            },
        },
        "price": {
            "amount": 5000,
            "currency": "GBP",
            "interval": {"unit": "Months", "count": 1, "times": 12},
        },
        "balance": {"amount": 5000},
        "pausePaymentDetail": {
            "reason": "Offering service for free to customer",
            "resumeAtTimestamp": 1470989538,
            "pausedAtTimestamp": 1470989538,
        },
        "cancelDetail": {
            "reason": "Customer no longer wants to use the service",
            "cancelledAtTimestamp": 1480989538,
        },
        "billingDetail": {
            "totalCycles": 12,
            "currentCycle": 4,
            "currentCycleStartTimestamp": 1480989538,
            "currentCycleEndTimestamp": 1480989538,
            "billingCycleTimestamp": 1480989538,
            "nextBillingTimestamp": 1480989538,
            "failureDetail": {
                "paymentAttempts": 2,
                "lastPaymentError": "insufficient_funds",
            },
        },
        "shippingDetails": {
            "address": {
                "firstName": "Fox",
                "lastName": "Mulder",
                "lineOne": "Stonehenge",
                "postalCode": "SP4 7DE",
                "city": "Salisbury",
                "country": "GB",
            }
        },
        "metadata": {"myCustomerId": "1"},
        "paymentSettings": {
            "statementDescriptor": {"descriptor": "Ryft Ltd", "city": "London"}
        },
        "createdTimestamp": 1470989538,
    }


def mock_subscriptions_resp():
    return {
        "items": [mock_subscription_resp()],
    }
