from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from .category_enum import Category
from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class Product(Base):
    __tablename__ = "product"

    id : Mapped[str] = sa.Column(sa.String, primary_key=True, default=generate_random_uuid)
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    name: Mapped[str] = sa.Column(sa.String, nullable=False, unique=False)
    price: Mapped[float] = sa.Column(sa.String, nullable=True, unique=False)
    category: Mapped[Category] = sa.Column(sa.Enum(Category), nullable=False, unique=False)
    quantity: Mapped[int] = sa.Column(sa.String, nullable=True, unique=False)
    added_user_id = sa.Column(sa.String, nullable=False)


