from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import (
    created_at,
    intpk,
    updated_at,
)

if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.interests import (
        InterestsDb,
    )
    from src.beta.infrastructure.data_access.models.user import UsersDb


class FormsDb(BaseDb):
    __tablename__ = "forms"

    id: Mapped[intpk]
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    is_visible: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    gender_id: Mapped[int] = mapped_column(
        ForeignKey("genders.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    metro_id: Mapped[int] = mapped_column(
        ForeignKey("metros.id", ondelete="CASCADE")
    )

    user: Mapped["UsersDb"] = relationship(back_populates="form")
    interests: Mapped[List["InterestsDb"]] = relationship(
        back_populates="form"
    )
