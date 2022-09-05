from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models import Product
from fastapi import HTTPException, status
from .....celery_worker.worker import clear_cache_task



def remove_product_by_id_(
    product_id: str,
    db_session: Session,
    current_user: dict
):
    stmt = select(Product).where(Product.id == product_id)
    product: Product | None = db_session.execute(stmt).scalar_one_or_none()
    if product is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        db_session.delete(product)
        clear_cache_task.apply_async(args=[product_id])
        return True

