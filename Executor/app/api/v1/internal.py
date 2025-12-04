from fastapi import APIRouter, Response, status

from schemas.readiness import ReadinessStatus


router_healthcheck = APIRouter()


@router_healthcheck.get(
    "",
    tags=["healthcheck"],
    response_class=Response,
)
async def get_healthcheck() -> Response:
    return Response(
        content=ReadinessStatus.ok,
        status_code=status.HTTP_200_OK
    )
