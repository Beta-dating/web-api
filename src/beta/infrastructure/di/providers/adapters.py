from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.beta.domain.form.repositories import FormRepository
from src.beta.domain.user.repositories import UserRepository
from src.beta.infrastructure.config import DatabaseConfig
from src.beta.infrastructure.data_access.repositories.form import (
    SqlalchemyFormRepository,
)
from src.beta.infrastructure.data_access.repositories.user import (
    SqlalchemyUserRepository,
)


class SqlalchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self) -> DatabaseConfig:
        return DatabaseConfig.from_env()

    @provide(scope=Scope.APP)
    def provide_engine(self, config: DatabaseConfig) -> AsyncEngine:
        # PostgreSQL Максимум соединений по умолчанию - 100
        #  с данными настройками 4 воркера займут 40 соединений
        return create_async_engine(
            config.db_uri,
            pool_size=10,
            max_overflow=0,
            pool_pre_ping=True,
            connect_args={
                "timeout": 15,
                "command_timeout": 5,
                "server_settings": {
                    "jit": "off",
                    "application_name": "web-api",
                },
            },
        )

    @provide(scope=Scope.APP)
    def provide_sessionmaker(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=False)

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

    form_repository = provide(
        SqlalchemyFormRepository,
        scope=Scope.REQUEST,
        provides=FormRepository,
    )
