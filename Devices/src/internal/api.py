from ninja import Router
from ninja.responses import Response
from django.db import connection


internal_router = Router()


@internal_router.get(
    "/",
    tags=["healthcheck"],
    response={200: str}
)
def get_healthcheck(request) -> Response:
    return "OK"


@internal_router.get(
    "/db-healthcheck",
    tags=["healthcheck"],
    response={200: str, 500: str}
)
def get_db_healthcheck(request) -> Response:
    try:
        connection.ensure_connection()
    except Exception:
        return Response("ERROR", status=500)
    return Response("OK", status=200)
