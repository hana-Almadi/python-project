
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    username: str
    email: str | None
    first_name: str
    last_name: str | None
    nationality: str | None
    bio: str | None

    class Config:
        orm_mode = True


class UserCreateRequest(BaseModel):
    first_name: str
    username: str
    password: str


class UserLoginResponse(BaseModel):
    access_token: str

    class Config:
        orm_mode = True


class UserLoginRequest(BaseModel):
    username: str
    password: str


class PublicUserResponse(BaseModel):
    username: str | None
    first_name: str | None

    class Config:
        orm_mode = True

class UserUpdateRequest(BaseModel):
    first_name: str | None
    last_name: str | None
    nationality: str | None
    bio: str | None
    email: str | None
