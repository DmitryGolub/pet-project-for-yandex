from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.service import decode_token

bearer = HTTPBearer(auto_error=True)


def get_current_username(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
) -> str:
    try:
        payload = decode_token(creds.credentials)
        username = payload.get("sub")
        if not username:
            raise ValueError("Token has no subject")
        return str(username)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
