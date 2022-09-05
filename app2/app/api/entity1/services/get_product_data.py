from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from commons.redis_client import RedisClient

from ..models import Product


def get_product_data_(
        db_session: Session,
        product_id: str,
        redis_client: RedisClient,
        current_user: dict
):
    cache_Data = redis_client.get_data(product_id)
    if cache_Data is None:
        print("no data in cache")
        stmt = select(Product).where(Product.id == product_id)
        product: Product | None = db_session.execute(stmt).scalar_one_or_none()
        if product is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            redis_client.cache_data(product_id,
                                    dict(
                                        id=product.id,
                                        name=product.name,
                                        created=product.created,
                                        price=product.price,
                                        category=product.category,
                                        added_user_id=product.added_user_id,
                                        quantity=product.quantity
                                    ))
            return product
    else:
        print("return cache data")
        return cache_Data
