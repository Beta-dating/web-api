from dataclasses import dataclass
from typing import List, Literal

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
class Age(ValueObject[int]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), int):
            raise DomainValidationError(
                f"Age must be an integer, not {type(self.to_raw())}"
            )
        if self.to_raw() < 18:
            raise DomainValidationError(
                f"Age must be more 18, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Description(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Description must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) < 0:
            raise DomainValidationError(
                f"Description must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Interests(ValueObject[List[str]]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Interests must be a List[str], not {type(self.to_raw())}"
            )


@dataclass(frozen=True)
class FirstName(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"First name must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) < 0:
            raise DomainValidationError(
                f"First name must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class Metro(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Metro must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) < 0:
            raise DomainValidationError(
                f"Metro must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class LastName(ValueObject[str]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"Last name must be a str, not {type(self.to_raw())}"
            )
        if len(self.to_raw()) < 0:
            raise DomainValidationError(
                f"Last name must be more 0 letters, not {self.to_raw()}"
            )


@dataclass(frozen=True)
class IsVisible(ValueObject[bool]):
    def validate(self) -> None:
        if not isinstance(self.to_raw(), bool):
            raise DomainValidationError(
                f"Is visible field must be a bool, not {type(self.to_raw())}"
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


GenderT = Literal["Male", "Female", "Empty"]
