from app.schemas import UserCreate, UserUpdate
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
    get_user_by_id,
    get_users,
    update_user,
    delete_user,
)

# CRUD operations for User model
def test_create_user(db_session):
    user_data = UserCreate(
        email= "testuser@example.com",
        username= "testuser",
        age= 30,
        password= "testpassword",
        initial_weight= 70.5,
    )
    user = create_user(db_session, user_data)
    assert user.username == user_data.username
    assert user.email == user_data.email
    assert user.age == user_data.age
    assert user.initial_weight == user_data.initial_weight
    assert user.hashed_password is not None
    assert user.id is not None

# get_user_by_email
def test_get_user_by_email(db_session, users):
    email_get = users[-1].email
    user = get_user_by_email(db_session, email_get)
    assert user.email == email_get
    assert user.username == users[-1].username
    assert user.age == users[-1].age
    assert user.initial_weight == users[-1].initial_weight
    assert user.hashed_password is not None
    assert user.id == users[-1].id

# get_user_by_id
def test_get_user_by_id(db_session, users):
    user_id = users[-1].id
    user = get_user_by_id(db_session, user_id)
    assert user.email == users[-1].email
    assert user.username == users[-1].username
    assert user.age == users[-1].age
    assert user.initial_weight == users[-1].initial_weight
    assert user.hashed_password is not None
    assert user.id == user_id

# get_users
def test_get_users(db_session, users):
    db_users = get_users(db_session)
    assert len(db_users) == len(users)
    for i in range(len(users)):
        assert db_users[i].email == users[i].email
        assert db_users[i].username == users[i].username
        assert db_users[i].age == users[i].age
        assert db_users[i].initial_weight == users[i].initial_weight
        assert db_users[i].hashed_password is not None
        assert db_users[i].id == users[i].id

# Update a user
def test_update_user(db_session, users):
    user_id = users[-1].id
    user_data = UserUpdate(
        username= "updated_username",
        email= "updated_emaill@example.com",
        age= 35,
        initial_weight= 75.5,
    )
    updated_user = update_user(db_session, user_id, user_data)
    assert updated_user.username == user_data.username
    assert updated_user.email == user_data.email
    assert updated_user.age == user_data.age
    assert updated_user.initial_weight == user_data.initial_weight
    assert updated_user.hashed_password is not None
    assert updated_user.id == user_id

# Delete a user
def test_delete_user(db_session, users):
    user_id = users[-1].id

    deleted_user = delete_user(db_session, user_id)
    assert deleted_user.id == user_id
    assert deleted_user.email == users[-1].email
    assert deleted_user.username == users[-1].username
    assert deleted_user.age == users[-1].age
    assert deleted_user.initial_weight == users[-1].initial_weight
    assert deleted_user.hashed_password is not None
    assert deleted_user.id == user_id
    assert get_user_by_id(db_session, user_id) ==  None

