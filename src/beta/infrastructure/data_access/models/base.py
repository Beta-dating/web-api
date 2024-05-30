from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import DateTime, func


class BaseDb(AsyncAttrs, DeclarativeBase):
    """Base class for all database models."""

    # Время будет указано как у начала транзакции, а не действительной вставки в бд, подробнее ниже
    # https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
