
from database import get_db


def get_pagination(
    limit: int = 10,
    offset: int = 0
):
    return {
        "limit": limit,
        "offset": offset
    }


def get_api_key(api_key: str):
    if api_key != "day5-secret-key":
        from fastapi import HTTPException, status

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )

    return api_key
