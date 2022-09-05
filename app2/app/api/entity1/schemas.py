from pydantic import BaseModel

from .category_enum import Category


class ProductCreateRequest(BaseModel):
    name: str
    category: Category
    added_user_id: str
    price: float
    quantity: int

    class Config:
        orm_mode = True


class ProductUpdateRequest(BaseModel):
    id: str
    price: float
    quantity: int


class ProductResponse(BaseModel):
    id: str
    name: str
    category: Category
    price: float
    quantity: int
    added_user_id: str

    class Config:
        orm_mode = True
