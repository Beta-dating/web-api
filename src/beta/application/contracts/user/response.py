from dataclasses import dataclass
from datetime import datetime

from src.beta.domain.user.entities import User


@dataclass(frozen=True)
class UserResponse:
    id: int
    tg_username: str
    is_blocked: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: User) -> "UserResponse":
        return UserResponse(
            id=entity.id.to_raw(),
            tg_username=entity.tg_username.to_raw(),
            is_blocked=entity.is_blocked.to_raw(),
            is_verified=entity.is_verified.to_raw(),
            created_at=entity.created_at.to_raw(),
            updated_at=entity.updated_at.to_raw(),
        )
