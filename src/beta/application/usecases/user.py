from src.beta.application.contracts.user.request import CreateUserRequest
from src.beta.application.contracts.user.response import UserResponse
from src.beta.application.protocols.interactor import Interactor
from src.beta.domain.user.repositories import UserRepository


class CreateUser(Interactor[CreateUserRequest, UserResponse]):
    def __init__(self, item_repository: UserRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: CreateUserRequest) -> UserResponse:
        user = await self.item_repository.create_user(
            tg_username=request.tg_username,
            is_blocked=request.is_blocked,
            is_verified=request.is_verified,
        )

        return UserResponse.from_entity(user)
