from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.beta.domain.user.entities import User
from src.beta.domain.user.repositories import UserRepository
from src.beta.infrastructure.data_access.models.user import UsersDb


class SqlalchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(self, username: str, is_blocked: bool) -> User:
        stmt = ((insert(UserDb)
                 .values(username=username, is_blocked=is_blocked))
                 .returning(UserDb.id, UserDb.username, UserDb.is_blocked))

        result = await self.session.execute(stmt)
        await self.session.commit()

        result = result.mappings().first()

        return User.create(
            id=result.id,
            username=result.username,
            is_blocked=result.is_blocked,
        )
