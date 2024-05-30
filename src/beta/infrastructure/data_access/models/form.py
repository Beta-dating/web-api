from typing import cast

from sqlalchemy.orm import Mapped, mapped_column

from src.beta.domain.form.entities import Form
from src.beta.domain.form.value_objects import GenderT
from src.beta.infrastructure.data_access.models.base import Base


class FormDb(Base):
    __tablename__ = "form"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    custom_name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[bool] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    preference: Mapped[str] = mapped_column(nullable=False)

    def to_entity(self) -> Form:
        return Form.create(
            id=cast(int, self.id),
            custom_name=cast(str, self.custom_name),
            gender=cast(GenderT, self.gender),
            age=cast(int, self.age),
            description=cast(str, self.description),
            is_active=cast(bool, self.is_active),
            preference=cast(str, self.preference),
        )
