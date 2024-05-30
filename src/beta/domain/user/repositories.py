from typing import Protocol

from src.beta.domain.user.entities import User


class UserRepository(Protocol):
    async def create_user(self, username: str, is_blocked: bool) -> User:
        raise NotImplementedError
