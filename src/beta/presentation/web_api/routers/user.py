from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.beta.application.contracts.user.request import (
    CreateUserRequest,
    GetUserByIdRequest,
)
from src.beta.application.contracts.user.response import UserResponse
from src.beta.application.usecases.user import CreateUser, GetUserById
from src.beta.presentation.web_api.schemas.user import UserCreateSchema

user_router = APIRouter(tags=["user"], route_class=DishkaRoute)


@user_router.post(
    "/user", response_model=UserResponse, description="Create an user"
)
async def create_user(
    schema: UserCreateSchema, interactor: FromDishka[CreateUser]
) -> UserResponse:
    return await interactor(
        CreateUserRequest(
            tg_username=schema.tg_username,
            is_blocked=schema.is_blocked,
            is_verified=schema.is_verified,
        )
    )


@user_router.get(
    "/user/{user_id}",
    response_model=UserResponse,
    description="Get user by id",
)
async def get_user_by_id(
    user_id: int, interactor: FromDishka[GetUserById]
) -> UserResponse:
    return await interactor(GetUserByIdRequest(id=user_id))
