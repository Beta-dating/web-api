from dataclasses import dataclass

from beta.domain.common.exceptions import DomainValidationError
from beta.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject[int]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise DomainValidationError(
                f"User id must be an integer, not {type(self.to_raw())}"
            )
        if self.to_raw() < 0:
            raise DomainValidationError(
                f"User id must be positive, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Username(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Username must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) < 0:
            raise DomainValidationError(
                f"Username must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class IsBlocked(ValueObject[bool]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"IsBlocked field must be a bool, not {type(self.to_raw())}"
            )
