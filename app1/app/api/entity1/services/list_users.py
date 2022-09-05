from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import User


def list_users_(
        db_session: Session
):
    stmt = select(User).order_by(User.created.desc())
    users: list[User] = db_session.execute(stmt).scalars().all()
    return users
