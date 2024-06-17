from typing import cast, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import intpk, created_at, updated_at

if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.form import FormsDb
    from src.beta.infrastructure.data_access.models.users_reactions import UsersReactionsDb
    from src.beta.infrastructure.data_access.models.preferences import PreferencesDb


class UsersDb(BaseDb):
    __tablename__ = "users"

    id: Mapped[intpk]
    tg_username: Mapped[str] = mapped_column(nullable=False)
    is_blocked: Mapped[bool] = mapped_column(nullable=False)
    is_verified: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    form: Mapped["FormsDb"] = relationship(back_populates="user")
    reactions: Mapped[list["UsersReactionsDb"]] = relationship(back_populates="user")
    preference: Mapped["PreferencesDb"] = relationship(back_populates="user")


