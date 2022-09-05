from fastapi import APIRouter, Depends, status

from .schemas import (UserCreateRequest,
                      UserLoginResponse,
                      UserLoginRequest,
                      UserResponse,
                      PublicUserResponse,
                      UserUpdateRequest)

from .services.signup import signup_

from .services.login import login_

from .services.list_users import list_users_

from .services.get_current_user_data import get_current_user_data_

from .services.update_current_user_data import update_current_user_data_

from fastapi.security import HTTPBearer

from ...common.dependencies import get_db_session,get_redis_client,get_verified_current_user_or_none

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post(
    path="/signup",
    response_model=UserResponse,
    responses={
        status.HTTP_200_OK: {"description": "user created", "model": UserResponse},
        status.HTTP_409_CONFLICT: {"description": "username already used"},
    }
)
def signup(
        body: UserCreateRequest,
        db_session=Depends(get_db_session),
):
    return signup_(body, db_session)


@user_router.post(
    path="/login",
    response_model=UserLoginResponse,
    responses={
        status.HTTP_200_OK: {"description": "valid credentials", "model": UserLoginResponse},
        status.HTTP_401_UNAUTHORIZED: {"description": "invalid credentials"},
    }
)
def login(
        body: UserLoginRequest,
        db_session=Depends(get_db_session),
):
    return login_(body, db_session)


@user_router.get(
    path="/me",
    response_model=UserResponse,
    dependencies=[Depends(HTTPBearer())],
)
def get_current_user_data(
        db_session=Depends(get_db_session),
        current_user=Depends(get_verified_current_user_or_none),
        redis_client=Depends(get_redis_client),
):
    return get_current_user_data_(db_session, current_user,redis_client)


@user_router.get(
    path="/",
    response_model=list[PublicUserResponse],
)
def list_users(
        db_session=Depends(get_db_session)
):
    return list_users_(db_session)


@user_router.patch(
    path="",
    response_model=UserResponse,
    dependencies=[Depends(HTTPBearer())],
)
def update_current_user_data(
        body: UserUpdateRequest,
        db_session=Depends(get_db_session),
        current_user=Depends(get_verified_current_user_or_none),
        redis_client=Depends(get_redis_client)
):
    return update_current_user_data_(body,
                                     db_session,
                                     current_user,
                                     redis_client)
