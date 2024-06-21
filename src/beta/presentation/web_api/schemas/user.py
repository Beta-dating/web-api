from datetime import datetime

from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    tg_username: str
    is_blocked: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
