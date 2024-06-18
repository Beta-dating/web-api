from dishka import AsyncContainer, make_async_container

from src.beta.infrastructure.di.providers.adapters import SqlalchemyProvider
from src.beta.infrastructure.di.providers.usecases import UseCasesProvider


def container_factory() -> AsyncContainer:
    return make_async_container(SqlalchemyProvider(), UseCasesProvider())