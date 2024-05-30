from dataclasses import dataclass

from src.beta.domain.user.entities import User


@dataclass(frozen=True)
class UserResponse:
    id: int
    username: str
    is_blocked: bool

    @staticmethod
    def from_entity(entity: User) -> "UserResponse":
        return UserResponse(
            id=entity.id.to_raw(),
            username=entity.username.to_raw(),
            is_blocked=entity.is_blocked.to_raw(),
        )
