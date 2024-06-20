from typing import cast, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import intpk
if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.preferences import PreferencesDb
    from src.beta.infrastructure.data_access.models.interests import InterestsDb


class UsersInterestsDb(BaseDb):
    __tablename__ = "users_interests"

    id: Mapped[intpk]

    preference_id: Mapped[int] = mapped_column(ForeignKey("preferences.id", ondelete="CASCADE"))
    interest_id: Mapped[int] = mapped_column(ForeignKey("interests.id", ondelete="CASCADE"))

    preference: Mapped["PreferencesDb"] = relationship(back_populates="user_interests")
    interest: Mapped["InterestsDb"] = relationship(back_populates="user_interests")
