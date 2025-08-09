def mock_create_account_request_hosted_onboarding_minimum():
    return {"email": "test@example.com"}


def mock_create_account_request_hosted_onboarding_business():
    return {
        "onboardingFlow": "Hosted",
        "entityType": "Business",
        "business": {
            "name": "Test Ltd",
            "type": "PublicCompany",
            "registrationNumber": "12345678",
            "registeredAddress": {
                "lineOne": "123 Street",
                "city": "Manchester",
                "country": "GB",
                "postalCode": "M1 1AA",
            },
            "contactEmail": "contact@test.com",
        },
    }


def mock_create_account_request_hosted_onboarding_individual():
    return {
        "onboardingFlow": "Hosted",
        "entityType": "Individual",
        "individual": {
            "firstName": "Fred",
            "lastName": "Jones",
            "email": "fred.jones@example.com",
            "dateOfBirth": "1990-01-20",
            "gender": "Male",
            "nationalities": ["GB"],
            "address": {
                "lineOne": "123 Road",
                "city": "London",
                "country": "GB",
                "postalCode": "SW1 1AA",
            },
        },
    }


def mock_create_account_request_non_hosted_onboarding_minimum():
    return {"onboardingFlow": "NonHosted"}


def mock_create_account_request_non_hosted_onboarding_business():
    return {
        "onboardingFlow": "NonHosted",
        "entityType": "Business",
        "business": {
            "name": "Test Ltd",
            "type": "PublicCompany",
            "registrationNumber": "12345678",
            "registeredAddress": {
                "lineOne": "123 Street",
                "city": "Manchester",
                "country": "GB",
                "postalCode": "M1 1AA",
            },
            "contactEmail": "contact@test.com",
        },
    }


def mock_create_account_request_non_hosted_onboarding_individual():
    return {
        "onboardingFlow": "NonHosted",
        "entityType": "Individual",
        "individual": {
            "firstName": "Fred",
            "lastName": "Jones",
            "email": "fred.jones@example.com",
            "dateOfBirth": "1990-01-20",
            "gender": "Male",
            "nationalities": ["GB"],
            "address": {
                "lineOne": "123 Road",
                "city": "London",
                "country": "GB",
                "postalCode": "SW1 1AA",
            },
        },
    }
