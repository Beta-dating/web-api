from dataclasses import dataclass, field

from fastapi import APIRouter

check_router = APIRouter(prefix="/check", tags=["check"])


@dataclass(frozen=True)
class Check:
    status: str = field(default="ok")


@check_router.get("/", response_model=Check)
async def health_check() -> Check:
    return Check(status="ok")
