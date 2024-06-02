from typing import cast, TYPE_CHECKING
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, DateTime, func

from src.beta.domain.user.entities import User
from src.beta.infrastructure.data_access.models.base import BaseDb

if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.form import FormDb


class UserDb(BaseDb):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    is_blocked: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    form: Mapped["FormDb"] = relationship(back_populates="user", lazy="selectin")

    def to_entity(self) -> User:
        return User.create(
            id=cast(int, self.id),
            username=cast(str, self.username),
            is_blocked=cast(bool, self.is_blocked),
        )
