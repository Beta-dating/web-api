from typing import List, Protocol

from src.beta.domain.form.entities import Form
from src.beta.domain.form.value_objects import GenderT


class FormRepository(Protocol):
    async def create_form(
        self,
        first_name: str,
        last_name: str,
        age: int,
        description: str,
        is_visible: bool,
        gender: GenderT,
        interests: List[str],
        metro: str,
    ) -> Form:
        raise NotImplementedError
