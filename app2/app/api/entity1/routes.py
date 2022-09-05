from fastapi import APIRouter, Depends, status

from ....app.common.dependencies import (get_verified_current_user_or_none,
                                         get_db_session,
                                         get_redis_client)

from .schemas import (ProductCreateRequest,
                      ProductUpdateRequest,
                      ProductResponse)
from fastapi.security import HTTPBearer
from .services.add_product import add_product_
from .services.update_product import update_product_
from .services.get_product_data import get_product_data_
from .services.get_user_products import get_user_products_
from .services.remove_product import remove_product_by_id_


product_router = APIRouter(prefix="/product", tags=["product"])


@product_router.post(
    path="/add",
    response_model=str,
    dependencies=[Depends(HTTPBearer())]
)
def add_product(
        body: ProductCreateRequest,
        db_session=Depends(get_db_session),
        current_user=Depends(get_verified_current_user_or_none),

):
    return add_product_(
        body,
        db_session,
        current_user
    )

@product_router.patch(
    path="/update",
    response_model=bool,
    dependencies=[Depends(HTTPBearer())]
)
def update_product(
        body: ProductUpdateRequest,
        db_session=Depends(get_db_session),
        current_user=Depends(get_verified_current_user_or_none),

):
    return update_product_(
        body,
        db_session,
        current_user
    )

@product_router.get(
    path="/{product_id}",
    response_model=ProductResponse,
    dependencies=[Depends(HTTPBearer())],
)
def get_product_data(
        product_id: str,
        db_session=Depends(get_db_session),
        redis_client=Depends(get_redis_client),
        current_user=Depends(get_verified_current_user_or_none),

):
    return get_product_data_(db_session,
                             product_id,
                             redis_client,
                             current_user)


@product_router.get(
    path="/user/list",
    response_model=list[ProductResponse],
    dependencies=[Depends(HTTPBearer())]

)
def list_user_products(
        db_session=Depends(get_db_session),
        current_user=Depends(get_verified_current_user_or_none),

):
    return get_user_products_(db_session,current_user)

@product_router.delete(
    path="/remove/{product_id}",
    response_model=bool,
    dependencies=[Depends(HTTPBearer())]
)
def remove_product(
        product_id: str,
        current_user=Depends(get_verified_current_user_or_none),
        db_session=Depends(get_db_session),

):
    return remove_product_by_id_(
        product_id,
        db_session,
        current_user
    )