from .db import db
from ..config import config
from commons.dependencies import get_db_session_dependency, get_redis_dependency
from typing import Optional
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer


get_db_read_session = get_db_session_dependency(db.ReadSessionLocal)
db_read_session = Depends(get_db_read_session)

get_db_session = get_db_session_dependency(db.SessionLocal)
db_session = Depends(get_db_session)

get_redis_client = get_redis_dependency(config=config)
redis_client = Depends(get_redis_client)


def get_verified_current_user_or_none(
    token: Optional[str] = Depends(OAuth2PasswordBearer(tokenUrl="user/login", auto_error=False))
):
    if token is None:
        return None

    try:
        varified_and_decoded_token = jwt.decode(token, config.AUTH_JWT_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return varified_and_decoded_token
