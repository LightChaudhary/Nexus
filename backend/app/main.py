from fastapi import FastAPI

from app.api.v1.router import api_router # routes
from app.core.config import settings # centralized configuration

# create and configure a fastapi application

def create_app() -> FastAPI:
    app = FastAPI(
        title= settings.PROJECT_NAME,
        version= settings.VERSION,
        docs_url= "/docs",
        redoc_url= "/redocs",
    )

    @app.get("/", tags=["root"])
    def root() -> dict:
        return {
            "service": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "docs": "/docs",
            "health": f"{settings.API_V1_PREFIX}/health",
        }

    app.include_router(
        api_router,
        prefix=settings.API_V1_PREFIX,
    )

    return app

app = create_app()
