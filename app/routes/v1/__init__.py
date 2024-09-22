from fastapi import APIRouter
from .endpoints import (
    root, login, register, dashboard,
    foods_config, meals_config, weights_view,
    activities_view
)


web_router = APIRouter()

web_router.include_router(root.router, prefix="", tags=["root"])
web_router.include_router(login.router, prefix="/login", tags=["login"])
web_router.include_router(register.router, prefix="/register", tags=["register"])
web_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
web_router.include_router(foods_config.router, prefix="/foods_configs", tags=["foods_configs"])
web_router.include_router(meals_config.router, prefix="/meals_configs", tags=["meals_configs"])
web_router.include_router(weights_view.router, prefix="/weights_view", tags=["weights_view"])
web_router.include_router(activities_view.router, prefix="/activities_view", tags=["activities_view"])
