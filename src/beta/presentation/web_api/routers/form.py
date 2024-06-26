from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.beta.application.contracts.form.request import CreateFormRequest
from src.beta.application.contracts.form.response import FormResponse
from src.beta.application.usecases.form import CreateForm
from src.beta.presentation.web_api.schemas.form import FormCreateForm

form_router = APIRouter(tags=["form"], route_class=DishkaRoute)


@form_router.post(
    "/form", response_model=FormResponse, description="Create a form"
)
async def create_form(
    schema: FormCreateForm, interactor: FromDishka[CreateForm]
) -> FormResponse:
    return await interactor(
        CreateFormRequest(
            first_name=schema.first_name,
            last_name=schema.last_name,
            age=schema.age,
            description=schema.description,
            is_visible=schema.is_visible,
            gender=schema.gender,
            interests=schema.interests,
            metro=schema.metro,
        )
    )
