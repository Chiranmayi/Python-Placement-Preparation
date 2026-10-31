
import os
import hashlib
import secrets

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader


# Read API key from environment variable
API_KEY = os.getenv("NOTES_API_KEY", "day5-secret-key")

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)


def verify_api_key(api_key: str = Security(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is missing"
        )

    if not secrets.compare_digest(api_key, API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return api_key


def hash_api_key(api_key: str) -> str:
    return hashlib.sha256(
        api_key.encode("utf-8")
    ).hexdigest()
