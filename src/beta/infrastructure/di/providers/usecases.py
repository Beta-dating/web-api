from dishka import Provider, Scope, provide

from src.beta.application.usecases.form import CreateForm
from src.beta.application.usecases.user import CreateUser, GetUserById


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    create_user = provide(CreateUser)
    get_user_by_id = provide(GetUserById)
    create_form = provide(CreateForm)
