from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.beta.domain.form.entities import Form


@dataclass(frozen=True)
class FormResponse:
    id: int
    first_name: str
    last_name: str
    age: int
    description: str
    is_visible: bool
    gender: str
    interests: List[str]
    metro: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: Form) -> "FormResponse":
        return FormResponse(
            id=entity.id.to_raw(),
            first_name=entity.first_name.to_raw(),
            last_name=entity.last_name.to_raw(),
            age=entity.age.to_raw(),
            description=entity.description.to_raw(),
            is_visible=entity.is_visible.to_raw(),
            gender=entity.gender.to_raw(),
            interests=entity.interests.to_raw(),
            metro=entity.metro.to_raw(),
            created_at=entity.created_at.to_raw(),
            updated_at=entity.updated_at.to_raw(),
        )
