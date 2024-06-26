from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import intpk

if TYPE_CHECKING:
    from src.beta.infrastructure.data_access.models.form import FormsDb


class MetrosDb(BaseDb):
    __tablename__ = "metros"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)

    form: Mapped["FormsDb"] = relationship(back_populates="metro")
