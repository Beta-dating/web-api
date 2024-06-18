from dataclasses import dataclass
from typing import Literal

from src.beta.domain.common.exceptions import DomainValidationError
from src.beta.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class FormId(ValueObject[int]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise DomainValidationError(
                f"Form id must be an integer, not {type(self.to_raw())}"
            )
        if self.to_raw() < 0:
            raise DomainValidationError(
                f"Form id must be positive, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class CustomName(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Custom name must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) < 0:
            raise DomainValidationError(
                f"Custom name must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Gender(ValueObject[bool]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), bool):
            raise DomainValidationError(
                f"Gender must be a bool, not {type(self.to_raw())}"
            )


@dataclass(frozen=True)
class Age(ValueObject[int]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise DomainValidationError(
                f"Age must be an integer, not {type(self.to_raw())}"
            )
        if self.to_raw() < 0:
            raise DomainValidationError(
                f"Age must be positive, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Description(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Description must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) <= 0:
            raise DomainValidationError(
                f"Description must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class IsActive(ValueObject[bool]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), bool):
            raise DomainValidationError(
                f"Is active must be a bool, not {type(self.to_raw())}"
            )


@dataclass(frozen=True)
class Preference(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Preference must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) <= 0:
            raise DomainValidationError(
                f"Preference must be more 0 letters, not {self.to_raw()}"
            )


GenderT = Literal["Male", "Female", "Empty"]
