from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.beta.domain.common.entities import Entity
from src.beta.domain.common.value_objects import CreatedAt, UpdatedAt
from src.beta.domain.form.value_objects import (
    Age,
    Description,
    FirstName,
    FormId,
    Gender,
    GenderT,
    Interests,
    IsVisible,
    LastName,
    Metro,
)


@dataclass
class Form(Entity[FormId]):
    first_name: str
    last_name: str
    age: int
    description: str
    is_visible: bool
    gender: GenderT
    interests: List[str]
    metro: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(
        id: int,
        first_name: str,
        last_name: str,
        age: int,
        description: str,
        is_visible: bool,
        gender: str,
        interests: List[str],
        metro: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> "Form":
        return Form(
            id=FormId(id),
            first_name=FirstName(first_name),
            last_name=LastName(last_name),
            age=Age(age),
            description=Description(description),
            is_visible=IsVisible(is_visible),
            gender=Gender(gender),
            interests=Interests(interests),
            metro=Metro(metro),
            created_at=CreatedAt(created_at),
            updated_at=UpdatedAt(updated_at),
        )
