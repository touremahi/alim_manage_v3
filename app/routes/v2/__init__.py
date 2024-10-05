from fastapi import APIRouter
from .endpoints import (
    root, login, register, dashboard,
    foods_config, meals_config
)


web_router = APIRouter()

web_router.include_router(root.router, prefix="", tags=["root"])
web_router.include_router(login.router, prefix="/login", tags=["login"])
web_router.include_router(register.router, prefix="/register", tags=["register"])
web_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
web_router.include_router(foods_config.router, prefix="/foods_configs", tags=["foods_configs"])
web_router.include_router(meals_config.router, prefix="/meals_configs", tags=["meals_configs"])