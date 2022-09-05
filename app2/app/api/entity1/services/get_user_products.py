from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Product

def get_user_products_(db_session: Session,
                       current_user: dict,

):
    stmt = select(Product).where(Product.added_user_id == current_user["id"]).order_by(Product.created.desc())
    products: list[Product] = db_session.execute(stmt).scalars().all()
    return products
