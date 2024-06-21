from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserRequest:
    tg_username: str
    is_blocked: bool
    is_verified: bool


@dataclass(frozen=True)
class GetUserByIdRequest:
    id: int
