from typing import cast
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, BigInteger, DateTime, func

from src.beta.domain.form.entities import Form
from src.beta.domain.form.value_objects import GenderT
from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.user import UserDb


class FormDb(BaseDb):
    __tablename__ = "form"

    id: Mapped[int] = mapped_column(primary_key=True)
    custom_name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[bool] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    preference: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("user.id", ondelete="CASCADE"), unique=True
    )

    user: Mapped["UserDb"] = relationship(back_populates="form", lazy="selectin")

    def to_entity(self) -> Form:
        return Form.create(
            id=cast(int, self.id),
            custom_name=cast(str, self.custom_name),
            gender=cast(GenderT, self.gender),
            age=cast(int, self.age),
            description=cast(str, self.description),
            is_active=cast(bool, self.is_active),
            preference=cast(str, self.preference),
            user_id=cast(int, self.user_id),
        )
