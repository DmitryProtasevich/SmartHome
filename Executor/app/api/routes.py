from fastapi import APIRouter

from api.v1 import internal
from core.config import settings


api_router_v1 = APIRouter(prefix=settings.API_PREFIX)

api_router_v1.include_router(
    internal.router_healthcheck,
    prefix="/internal",
)
