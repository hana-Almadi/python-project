from sqlalchemy.orm import Session
from ..schemas import ProductUpdateRequest
from ..models import Product
from sqlalchemy import select
from fastapi import HTTPException, status
from .....celery_worker.worker import clear_cache_task




def update_product_(
        body: ProductUpdateRequest,
        db_session: Session,
        current_user: dict
):
    stmt = select(Product).where(Product.id == body.id)
    product: Product | None = db_session.execute(stmt).scalar_one_or_none()
    if product is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        product.price = body.price
        product.quantity = body.quantity
        id = clear_cache_task.apply_async(args=[body.id])
        print(id)
        return True

