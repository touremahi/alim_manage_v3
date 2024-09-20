from app.schemas import UserCreate, UserUpdate
from app.services.user_service import (
    create_user_service,
    get_user_in_db_service,
    get_user_by_email_service,
    get_user_by_id_service,
    get_users_service,
    update_user_info,
    delete_user_service,
)

# Create a new user
def test_create_user_service(db_session):
    user_data = UserCreate(
        email= "testuser@example.com",
        username= "testuser",
        age= 30,
        password= "testpassword",
        initial_weight= 70.5
    )
    user = create_user_service(db_session, user_data)
    assert user.username == user_data.username
    assert user.email == user_data.email
    assert user.age == user_data.age
    assert user.initial_weight == user_data.initial_weight
    assert user.hashed_password is not None
    assert user.id is not None

#  get_user_by_email_service
def test_get_user_by_email_service(db_session, users):
    email_get = users[-1].email
    user = get_user_by_email_service(db_session, email_get)
    assert user.email == email_get
    assert user.username == users[-1].username
    assert user.age == users[-1].age
    assert user.initial_weight == users[-1].initial_weight
    assert user.id == users[-1].id

# get_user_by_id_service
def test_get_user_by_id_service(db_session, users):
    user_id = users[-1].id
    user = get_user_by_id_service(db_session, user_id)
    assert user.email == users[-1].email
    assert user.username == users[-1].username
    assert user.age == users[-1].age
    assert user.initial_weight == users[-1].initial_weight
    assert user.id == user_id

# get_users_service
def test_get_users_service(db_session, users):
    users_db = get_users_service(db_session)
    assert len(users_db) == len(users)
    for user_db, user in zip(users_db, users):
        assert user_db.email == user.email
        assert user_db.username == user.username
        assert user_db.age == user.age
        assert user_db.initial_weight == user.initial_weight
        assert user_db.id == user.id

# get_user_in_db_service
def test_get_user_in_db_service(db_session, users):
    user_email = users[-1].email
    user_db = get_user_in_db_service(db_session, user_email)
    assert user_db.email == user_email
    assert user_db.username == users[-1].username
    assert user_db.age == users[-1].age
    assert user_db.initial_weight == users[-1].initial_weight
    assert user_db.id == users[-1].id
    assert user_db.hashed_password == users[-1].hashed_password

# update_user_info
def test_update_user_info(db_session, users):
    user_id = users[-1].id
    user_update = UserUpdate(
        email= "updateduser@example.com",
        username= "updateduser",
        age= 35,
        initial_weight= 75.5
    )
    updated_user = update_user_info(db_session, user_id, user_update)
    assert updated_user.email == user_update.email
    assert updated_user.username == user_update.username
    assert updated_user.age == user_update.age
    assert updated_user.initial_weight == user_update.initial_weight
    assert updated_user.id == user_id

# delete_user_service
def test_delete_user_service(db_session, users):
    user_id = users[-1].id
    deleted_user = delete_user_service(db_session, user_id)
    assert deleted_user.id == user_id
    assert deleted_user.email == users[-1].email
    assert deleted_user.username == users[-1].username
    assert deleted_user.age == users[-1].age
    assert deleted_user.initial_weight == users[-1].initial_weight
    try:
        get_user_by_id_service(db_session, user_id)
    except ValueError as e:
        assert str(e) == "User not found"
        

