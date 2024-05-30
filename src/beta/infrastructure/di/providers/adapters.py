from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from src.beta.infrastructure.config import DatabaseConfig
from src.beta.domain.user.repositories import UserRepository
from src.beta.infrastructure.data_access.repositories.user import SqlalchemyUserRepository


class SqlalchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self) -> DatabaseConfig:
        return DatabaseConfig.from_env()

    @provide(scope=Scope.APP)
    def provide_engine(self, config: DatabaseConfig) -> AsyncEngine:
        return create_async_engine(config.db_uri)

    @provide(scope=Scope.APP)
    def provide_sessionmaker(
            self, engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine, expire_on_commit=False, class_=AsyncSession,
        )

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
            self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    user_repository = provide(
        SqlalchemyUserRepository,
        scope=Scope.REQUEST,
        provides=UserRepository,
    )
