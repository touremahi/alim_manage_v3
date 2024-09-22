from fastapi import APIRouter
from .endpoints import (
    auth, users, meals, meal_foods,
    foods, meal_contents, activities, weights
)

api_router = APIRouter()

# Inclure les différentes routes
# api_router.include_router(auth.router, prefix="/auth", tags=["authentification"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(foods.router, prefix="/foods", tags=["foods"])
api_router.include_router(meals.router, prefix="/meals", tags=["meals"])
api_router.include_router(meal_foods.router, prefix="/meal_foods", tags=["meal_foods"])
api_router.include_router(meal_contents.router, prefix="/meal_contents", tags=["meal_contents"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
api_router.include_router(weights.router, prefix="/weights", tags=["weights"])
