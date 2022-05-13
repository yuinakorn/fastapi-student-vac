from fastapi import APIRouter
from routes.token import token_controller

router = APIRouter(prefix="/login", tags=["login"])


@router.get("/login/")
def to_get_token(password_hash: str, user: str):
    return token_controller.get_your_token(password_hash, user)
