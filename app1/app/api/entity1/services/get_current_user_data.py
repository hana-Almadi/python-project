from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from commons.redis_client import RedisClient

from ..models import User


def get_current_user_data_(
        db_session: Session,
        current_user: dict,
        redis_client: RedisClient
):
    cache_Data = redis_client.get_data(current_user["id"])
    if cache_Data is None:
        print("no data in cache")
        stmt = select(User).where(User.id == current_user["id"])
        user: User | None = db_session.execute(stmt).scalar_one_or_none()
        if user is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            redis_client.cache_data(current_user["id"],
                                    dict(
                                        id=user.id,
                                        username=user.username,
                                        email=user.email,
                                        first_name=user.first_name,
                                        last_name=user.last_name,
                                        nationality=user.nationality,
                                        bio=user.bio
                                    ))
            return user
    else:
        print("return cache data")
        return cache_Data
