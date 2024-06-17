from typing import cast
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, DateTime, func

from src.beta.domain.user.entities import User
from src.beta.infrastructure.data_access.models.base import BaseDb

from src.beta.infrastructure.data_access.models.form import FormDb


class UserDb(BaseDb):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    tg_username: Mapped[str] = mapped_column(nullable=False)
    is_blocked: Mapped[bool] = mapped_column(nullable=False)
    is_verified: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
