from dataclasses import dataclass

from beta.domain.common.entities import Entity
from beta.domain.form.value_objects import (FormId,
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

    @staticmethod
    def create(
            id: int,
            custom_name: str,
            gender: GenderT,
            age: int,
            description: str,
            is_active: bool,
            preference: str,
    ) -> "Form":
        return Form(
            id=FormId(id),
            custom_name=CustomName(custom_name),
            gender=Gender(gender),
            age=Age(age),
            description=Description(description),
            is_active=IsActive(is_active),
            preference=Preference(preference),
        )
