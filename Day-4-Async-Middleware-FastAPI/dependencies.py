from fastapi import Depends, HTTPException


# Main dependency
def get_current_user():

    return {
        "id": 101,
        "username": "Chiranmayi",
        "role": "admin"
    }


# Sub-dependency
def require_admin(user=Depends(get_current_user)):

    if user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user


# Reusable pagination dependency
def common_pagination(skip: int = 0, limit: int = 10):

    return {
        "skip": max(skip, 0),
        "limit": min(max(limit, 1), 100)
    }