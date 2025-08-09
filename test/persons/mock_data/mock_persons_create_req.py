def mock_create_persons_req():
    return {
        "firstName": "Fred",
        "middleNames": "David",
        "lastName": "Jones",
        "email": "fred.jones@example.com",
        "dateOfBirth": "1990-01-20",
        "countryOfBirth": "GB",
        "gender": "Male",
        "nationalities": ["GB"],
        "address": {
            "lineOne": "string",
            "lineTwo": "string",
            "city": "string",
            "country": "GB",
            "postalCode": "string",
            "region": "string",
        },
        "phoneNumber": "string",
        "businessRoles": ["BusinessContact", "Director"],
        "documents": [
            {
                "type": "BankStatement",
                "front": "fl_01G0EYVFR02KBBVE2YWQ8AKMGJ",
                "back": "fl_01G0EYVFR02KBBVE2YWQ8AKMGJ",
                "country": "GB",
            }
        ],
        "metadata": {"accountId": "1"},
    }
