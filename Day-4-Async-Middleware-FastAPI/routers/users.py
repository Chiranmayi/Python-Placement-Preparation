from fastapi import APIRouter, Depends
from dependencies import get_current_user, require_admin

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/profile")
def get_profile(user=Depends(get_current_user)):

    return {
        "message": "User profile fetched successfully",
        "user": user
    }


@router.get("/admin")
def admin_dashboard(user=Depends(require_admin)):

    return {
        "message": "Welcome to admin dashboard",
        "user_id": user["id"],
        "role": user["role"]
    }