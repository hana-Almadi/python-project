
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..helpers import hash_password
from ..models import User
from ..schemas import UserCreateRequest


def signup_(
        body: UserCreateRequest,
        db_session: Session):
    user = User(
        first_name = body.first_name,
        hashed_password = hash_password(body.password),
        username = body.username)

    db_session.add(user)

    try:
        db_session.flush()
        return user
    except IntegrityError:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "username already used")
