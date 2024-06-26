from dataclasses import dataclass
from datetime import datetime
from typing import Generic, TypeVar

ValueT = TypeVar("ValueT")


@dataclass(frozen=True)
class ValueObject(Generic[ValueT]):
    __value: ValueT

    def to_raw(self) -> ValueT:
        return self.__value

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        """
        Must be implemented by subclasses.
        Raises a :class`DomainValidationError` if the value is invalid.
        """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_raw()!r})"


@dataclass(frozen=True)
class CreatedAt(ValueObject[datetime]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), datetime):
            raise DomainValidationError(
                f"Created at field must be a datetime, not {type(self.to_raw())}"
            )


@dataclass(frozen=True)
class UpdatedAt(ValueObject[datetime]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), datetime):
            raise DomainValidationError(
                f"Updated at field must be a datetime, not {type(self.to_raw())}"
            )
