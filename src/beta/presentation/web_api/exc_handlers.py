from typing import cast

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler

from src.beta.domain.common.exceptions import DomainValidationError


async def domain_validation_handler(
    exc: DomainValidationError,
) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": exc.message})


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        DomainValidationError,
        cast(ExceptionHandler, domain_validation_handler),
    )
