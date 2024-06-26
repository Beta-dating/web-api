from datetime import datetime
from typing import List

from pydantic import BaseModel


class FormCreateForm(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    description: str
    is_visible: bool
    gender: str
    interests: List[str]
    metro: str
