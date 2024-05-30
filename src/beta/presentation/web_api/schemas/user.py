from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    is_blocked: bool
