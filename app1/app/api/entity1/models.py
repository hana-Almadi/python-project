from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from commons.utils.generate_random_id_uuid import generate_random_uuid
from commons.db import Base



class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = sa.Column(sa.String, primary_key=True, default=generate_random_uuid)  # type: ignore
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    username: Mapped[str] = sa.Column(sa.String, nullable=False, unique=True)  # type: ignore
    hashed_password: Mapped[str] = sa.Column(sa.String, nullable=False)  # type: ignore
    email: Mapped[str] = sa.Column(sa.String, nullable=True, unique=False)  # type: ignore
    first_name: Mapped[str] = sa.Column(sa.String, nullable=True, unique=False)  # type: ignore
    last_name: Mapped[str] = sa.Column(sa.String, nullable=True, unique=False)  # type: ignore
    bio: Mapped[str] = sa.Column(sa.String, nullable=True, unique=False)  # type: ignore
    nationality: Mapped[str] = sa.Column(sa.String, nullable=True, unique=False)  # type: ignore




