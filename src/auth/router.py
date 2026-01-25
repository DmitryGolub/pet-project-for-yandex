from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.schemas import LoginRequest, TokenResponse, MeResponse
from src.auth.dependencies import get_current_username
from src.auth.service import create_access_token

from src.core.config import settings

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    if (
        payload.username != settings.USERNAME
        or payload.password != settings.PASSWORD
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token(subject=payload.username)
    return TokenResponse(access_token=token)


@router.get("/me", response_model=MeResponse)
def me(username: str = Depends(get_current_username)):
    return MeResponse(username=username)
