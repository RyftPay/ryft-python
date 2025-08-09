from ryft_sdk.models.errors import RyftError


def mock_ryft_error():
    return RyftError(
        400,
        {
            "requestId": "123456",
            "code": "InvalidRequest",
            "status": 400,
            "errors": [
                {
                    "message": "Invalid field value",
                }
            ],
        },
    )
