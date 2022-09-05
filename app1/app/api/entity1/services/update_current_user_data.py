from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..schemas import UserUpdateRequest

from ..models import User
from commons.redis_client import RedisClient


def update_current_user_data_(
        body: UserUpdateRequest,
        db_session: Session,
        current_user: dict,
        redis_client: RedisClient

):
    stmt = select(User).where(User.id == current_user["id"])
    user: User | None = db_session.execute(stmt).scalar_one_or_none()
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        user.first_name = body.first_name
        user.last_name = body.last_name
        user.nationality = body.nationality
        user.bio = body.bio
        user.email = body.email
        redis_client.clear_cache(current_user["id"])
    return user
