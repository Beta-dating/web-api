from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserRequest:
    username: str
    is_blocked: bool
