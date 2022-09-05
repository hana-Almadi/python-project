from sqlalchemy.orm import Session
from ..schemas import ProductCreateRequest
from ..models import Product
from sqlalchemy.exc import IntegrityError


def add_product_(
    body: ProductCreateRequest,
    db_session: Session,
    current_user: dict
):
    userId = current_user["id"]
    product = Product(
        name = body.name,
        added_user_id = userId,
        category = body.category,
        price = body.price,
        quantity = body.quantity
    )
    db_session.add(product)

    try:
        db_session.flush()
        return product.id
    except IntegrityError:
        raise Exception()