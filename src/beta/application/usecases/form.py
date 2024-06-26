from src.beta.application.contracts.form.request import CreateFormRequest
from src.beta.application.contracts.form.response import FormResponse
from src.beta.application.protocols.interactor import Interactor
from src.beta.domain.form.repositories import FormRepository


class CreateForm(Interactor[CreateFormRequest, FormResponse]):
    def __init__(self, item_repository: FormRepository) -> None:
        self.item_repository = item_repository

    async def __call__(self, request: CreateFormRequest) -> FormResponse:
        form = await self.item_repository.create_form(
            first_name=request.first_name,
            last_name=request.last_name,
            age=request.age,
            description=request.description,
            is_visible=request.is_visible,
            gender=request.gender,
            interests=request.interests,
            metro=request.metro,
        )

        return FormResponse.from_entity(form)
