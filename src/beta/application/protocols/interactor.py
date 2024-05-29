from typing import Protocol, TypeVar

Request = TypeVar("Request", contravariant=True)
Response = TypeVar("Response", covariant=True)


class Interactor(Protocol[Request, Response]):
    async def __call__(self, request: Request) -> Response:
        raise NotImplementedError
