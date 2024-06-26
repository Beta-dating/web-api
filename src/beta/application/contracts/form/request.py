from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CreateFormRequest:
    first_name: str
    last_name: str
    age: int
    description: str
    is_visible: bool
    gender: str
    interests: List[str]
    metro: str
