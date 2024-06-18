from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import intpk
if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.user import UsersDb


class UsersReactionsDb(BaseDb):
    __tablename__ = "users_reactions"

    id: Mapped[intpk]
    to_tg_username: Mapped[str] = mapped_column(nullable=False)
    sign: Mapped[bool] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["UsersDb"] = relationship(back_populates="reactions")
