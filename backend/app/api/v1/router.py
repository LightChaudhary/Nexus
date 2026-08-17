from fastapi import APIRouter

from app.api.v1.health import health as health_router

# creating router that represents all api version 1 endpoints

api_router = APIRouter()

# take all routes from health_router and add them to api_router
api_router.include_router(
    health_router,
    tags=["health"],
)