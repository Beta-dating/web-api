from dataclasses import dataclass

from beta.domain.common.entities import Entity
from beta.domain.user.value_objects import UserId, Username, IsBlocked


@dataclass
class User(Entity[UserId]):
    username: str
    is_blocked: bool
    form_id: int

    @staticmethod
    def create(
            id: int,
            username: str,
            is_blocked: bool,
            form_id: int,
    ) -> "User":
        return User(
            id=UserId(id),
            username=Username(username),
            is_blocked=IsBlocked(is_blocked),
            form_id=form_id,
        )
