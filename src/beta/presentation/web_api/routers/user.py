from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.beta.application.contracts.user.request import CreateUserRequest
from src.beta.application.contracts.user.response import UserResponse
from src.beta.application.usecases.user import CreateUser
from src.beta.presentation.web_api.schemas.user import UserCreateSchema


user_router = APIRouter(tags=["user"], route_class=DishkaRoute)


@user_router.post(
    "/user",
    response_model=UserResponse,
    description="Create an user"
)
async def create_user(
        schema: UserCreateSchema, interactor: FromDishka[CreateUser]
) -> UserResponse:
    return await interactor(
        CreateUserRequest(
            username=schema.username,
            is_blocked=schema.is_blocked,
        )
    )
