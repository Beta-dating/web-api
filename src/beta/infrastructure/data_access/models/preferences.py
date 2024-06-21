from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import (
    created_at,
    intpk,
    updated_at,
)

if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.user import UsersDb
    from src.beta.infrastructure.data_access.models.users_interests import (
        UsersInterestsDb,
    )


class PreferencesDb(BaseDb):
    __tablename__ = "preferences"

    id: Mapped[intpk]
    gender_id: Mapped[int] = mapped_column(
        ForeignKey("genders.id", ondelete="CASCADE")
    )
    age_range_start: Mapped[int] = mapped_column(nullable=False)
    age_range_end: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    metro_id: Mapped[int] = mapped_column(
        ForeignKey("metros.id", ondelete="CASCADE")
    )

    user: Mapped["UsersDb"] = relationship(back_populates="preference")

    user_interests: Mapped["UsersInterestsDb"] = relationship(
        back_populates="preference"
    )
