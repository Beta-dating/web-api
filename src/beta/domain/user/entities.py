from dataclasses import dataclass
from datetime import datetime

from src.beta.domain.common.entities import Entity
from src.beta.domain.user.value_objects import (
    CreatedAt,
    IsBlocked,
    IsVerified,
    TgUsername,
    UpdatedAt,
    UserId,
)


@dataclass
class User(Entity[UserId]):
    tg_username: str
    is_blocked: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(
        id: int,
        tg_username: str,
        is_blocked: bool,
        is_verified: bool,
        created_at: datetime,
        updated_at: datetime,
    ) -> "User":
        return User(
            id=UserId(id),
            tg_username=TgUsername(tg_username),
            is_blocked=IsBlocked(is_blocked),
            is_verified=IsVerified(is_verified),
            created_at=CreatedAt(created_at),
            updated_at=UpdatedAt(updated_at),
        )
