from dishka import Provider, Scope, provide

from src.beta.application.usecases.user import CreateUser


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    create_user = provide(CreateUser)
