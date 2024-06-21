from typing import Protocol

from src.beta.domain.user.entities import User


class UserRepository(Protocol):
    async def create_user(
        self, tg_username: str, is_blocked: bool, is_verified: bool
    ) -> User:
        raise NotImplementedError

    async def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError
