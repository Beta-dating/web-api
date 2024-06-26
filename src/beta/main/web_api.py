from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.beta.infrastructure.di.main import container_factory
from src.beta.presentation.web_api.exc_handlers import init_exception_handlers
from src.beta.presentation.web_api.routers.check import check_router
from src.beta.presentation.web_api.routers.form import form_router
from src.beta.presentation.web_api.routers.user import user_router


def init_di(app: FastAPI) -> None:
    setup_dishka(container_factory(), app)


def init_routers(app: FastAPI) -> None:
    app.include_router(check_router)
    app.include_router(user_router)
    app.include_router(form_router)


def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)
    init_routers(app)
    init_exception_handlers(app)

    return app
