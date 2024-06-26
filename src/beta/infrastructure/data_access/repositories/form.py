from typing import List

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.beta.domain.form.entities import Form
from src.beta.domain.user.repositories import UserRepository
from src.beta.infrastructure.data_access.models.form import FormsDb


class SqlalchemyFormRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_form(
        self,
        first_name: str,
        last_name: str,
        age: int,
        description: str,
        is_visible: bool,
        gender: str,
        interests: List[str],
        metro: str,
    ) -> Form:
        stmt = (
            insert(FormsDb)
            .values(
                first_name=first_name,
                last_name=last_name,
                age=age,
                description=description,
                is_visible=is_visible,
                gender=gender,
                interests=interests,
                metro=metro,
            )
            .returning(
                FormsDb.id,
                FormsDb.first_name,
                FormsDb.last_name,
                FormsDb.age,
                FormsDb.description,
                FormsDb.is_visible,
                FormsDb.gender,
                FormsDb.interests,
                FormsDb.metro,
            )
        )

        result = await self.session.execute(stmt)
        await self.session.commit()

        result = result.scalars().first()

        return result.to_entity()
