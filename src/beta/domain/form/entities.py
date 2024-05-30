from dataclasses import dataclass

from src.beta.domain.common.entities import Entity
from src.beta.domain.form.value_objects import (FormId,
                                            CustomName,
                                            Gender,
                                            Age,
                                            Description,
                                            IsActive,
                                            Preference,
                                            GenderT
                                            )


@dataclass
class Form(Entity[FormId]):
    custom_name: str
    gender: GenderT
    age: int
    description: str
    is_active: bool
    preference: str
    user_id: int

    @staticmethod
    def create(
            id: int,
            custom_name: str,
            gender: GenderT,
            age: int,
            description: str,
            is_active: bool,
            preference: str,
            user_id: int
    ) -> "Form":
        return Form(
            id=FormId(id),
            custom_name=CustomName(custom_name),
            gender=Gender(gender),
            age=Age(age),
            description=Description(description),
            is_active=IsActive(is_active),
            preference=Preference(preference),
            user_id=user_id,
        )
