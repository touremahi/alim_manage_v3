import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.main import app
from app.db.base import Base
from app.db.session import get_db
from app.core.config import settings
from app.models import (
    User, Food, Meal,
    MealFood, Weight, Activity
)

# créer une base de données en mémoire pour les tests
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL_TEST
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer une session de base de données pour les tests
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# Remplacer la dépendant de base de données dans FastAPI par la session de test
@pytest.fixture(scope="function")
def client(db_session: Session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def users(db_session):
    user_data = [
        User(
            username="test1",
            email="email1@domain.com",
            age=31,
            hashed_password="password1",
            initial_weight=78
        ),
        User(
            username="test2",
            email="email2@domain.com",
            age=32,
            hashed_password="password2",
            initial_weight=79
        )
    ]
    db_session.add_all(user_data)
    db_session.commit()
    return user_data

@pytest.fixture(scope="function")
def foods(db_session):
    food_data = [
        Food(
            name="food1",
            unit="g",
            calories=10,
            category="Féculents"
        ),
        Food(
            name="food2",
            unit="ml",
            calories=12,
            category="Fruits"
        ),
        Food(
            name="food3",
            unit="g",
            calories=11,
            category="Fruits"
        )

    ]
    db_session.add_all(food_data)
    db_session.commit()
    return food_data

@pytest.fixture(scope="function")
def meals(db_session, users):
    meal_data = [
        Meal(
            user_id=user.id,
            date=datetime.date(2023, 1, 1),
            type=f"meal{key}",
            time=datetime.time(12, 0)
        ) for key, user in enumerate(users)
    ]
    db_session.add_all(meal_data)
    db_session.commit()
    return meal_data

@pytest.fixture(scope="function")
def meal_foods(db_session, meals, foods):
    meal_food_data = []
    for meal in meals:
        for food in foods:
            meal_food_data.append(
                MealFood(
                    meals=meal,
                    foods=food,
                    quantity=100
                )
            )
    db_session.add_all(meal_food_data)
    db_session.commit()
    return meal_food_data

@pytest.fixture(scope="function")
def activities(db_session, users):
    activity_data = [
        Activity(
            user_id=user.id,
            date=datetime.date(2023, 1, 1),
            activity_type=f"activity{key}",
            duration=datetime.timedelta(1, 0).total_seconds(),
            time=datetime.time(12, 0)
        ) for key, user in enumerate(users)
    ]
    db_session.add_all(activity_data)
    db_session.commit()
    return activity_data

@pytest.fixture(scope="function")
def weights(db_session, users):
    weight_data = [
        Weight(
            user_id=user.id,
            date=datetime.date(2023, 1, 1),
            weight=78
        ) for user in users
    ]
    db_session.add_all(weight_data)
    db_session.commit()
    return weight_data

