import uvicorn
from fastapi import FastAPI

from core.config import settings
from api.routes import api_router_v1

app = FastAPI()


def app_factory() -> FastAPI:

    app = FastAPI(
        docs_url=f"{settings.API_PREFIX}/docs/",
        openapi_url=f"{settings.API_PREFIX}/openapi.json/",
    )
    app.include_router(api_router_v1)

    return app


app = app_factory()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
