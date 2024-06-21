from sqlalchemy.orm import Mapped, mapped_column

from src.beta.infrastructure.data_access.models.base import BaseDb
from src.beta.infrastructure.data_access.models.types.types import intpk


class GendersDb(BaseDb):
    __tablename__ = "genders"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)
