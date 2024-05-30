from typing import cast

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from src.beta.domain.user.entities import User
from src.beta.infrastructure.data_access.models.base import Base


class UserDb(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    is_blocked: Mapped[bool] = mapped_column(nullable=False)

    def to_entity(self) -> User:
        return User.create(
            id=cast(int, self.id),
            username=cast(str, self.username),
            is_blocked=cast(bool, self.is_blocked),

        )


