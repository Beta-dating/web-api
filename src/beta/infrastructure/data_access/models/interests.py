from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import intpk

if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.form import FormsDb
    from src.beta.infrastructure.data_access.models.users_interests import (
        UsersInterestsDb,
    )


class InterestsDb(BaseDb):
    __tablename__ = "interests"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)

    form_id: Mapped[int] = mapped_column(ForeignKey("forms.id"))

    user_interests: Mapped["UsersInterestsDb"] = relationship(
        back_populates="interests"
    )
    form: Mapped["FormsDb"] = relationship(back_populates="interests")
