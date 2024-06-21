from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.beta.domain.user.entities import User
from src.beta.domain.user.repositories import UserRepository
from src.beta.infrastructure.data_access.models.user import UsersDb


class SqlalchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(
        self, tg_username: str, is_blocked: bool, is_verified: bool
    ) -> User:
        stmt = (
            insert(UsersDb).values(
                tg_username=tg_username,
                is_blocked=is_blocked,
                is_verified=is_verified,
            )
        ).returning(
            UsersDb.id,
            UsersDb.tg_username,
            UsersDb.is_blocked,
            UsersDb.is_verified,
            UsersDb.created_at,
            UsersDb.updated_at,
        )

        result = await self.session.execute(stmt)
        await self.session.commit()

        result = result.mappings().first()

        return User.create(
            id=result.id,
            tg_username=result.tg_username,
            is_blocked=result.is_blocked,
            is_verified=result.is_verified,
            created_at=result.created_at,
            updated_at=result.updated_at,
        )

    async def get_user_by_id(self, user_id: int) -> User:
        query = select(UsersDb).where(UsersDb.id == user_id)
        result = await self.session.execute(query)
        result = result.scalar()

        return result.to_entity()
