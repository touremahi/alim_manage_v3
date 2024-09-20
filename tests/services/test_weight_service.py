import datetime

from app.schemas import WeightCreate
from app.services.weight_service import (
    create_weight_service, get_weights_service,
    get_weight_by_id_service, get_weights_by_date_service,
    get_weights_by_user_service, update_weight_service,
    delete_weight_service
)

# Test create weight
def test_create_weight(db_session, users):
    weight_data = WeightCreate(
        user_id=users[-1].id,
        weight=70.5,
        date=datetime.date(2024, 9, 21)
    )
    weight = create_weight_service(db_session, weight_data)
    assert weight.user_id == users[-1].id
    assert weight.weight == 70.5
    assert weight.date == datetime.date(2024, 9, 21)
    assert weight.id is not None

# Test get weights
def test_get_weights(db_session, weights):
    weights = get_weights_service(db_session)
    assert len(weights) == len(weights)
    for weight in weights:
        assert weight.id is not None
        assert weight.user_id is not None
        assert weight.weight is not None
        assert weight.date is not None

# Test get weight by ID
def test_get_weight_by_id(db_session, weights):
    weight_id = weights[-1].id
    weight = get_weight_by_id_service(db_session, weight_id)
    assert weight.id == weight_id
    assert weight.user_id == weights[-1].user_id
    assert weight.weight == weights[-1].weight
    assert weight.date == weights[-1].date

# Test get weights by date
def test_get_weights_by_date(db_session, weights):
    date = weights[-1].date
    weights = get_weights_by_date_service(db_session, date)
    assert len(weights) == len(weights)
    for weight in weights:
        assert weight.date == date
        assert weight.user_id is not None
        assert weight.weight is not None
        assert weight.id is not None

# Test get weights by user
def test_get_weights_by_user(db_session, weights):
    user_id = weights[-1].user_id
    weights = get_weights_by_user_service(db_session, user_id)
    assert len(weights) == len(weights)
    for weight in weights:
        assert weight.user_id == user_id
        assert weight.weight is not None
        assert weight.date is not None
        assert weight.id is not None

# Test update weight
def test_update_weight(db_session, weights):
    weight_id = weights[-1].id
    weight_data = WeightCreate(
        user_id=weights[-1].user_id,
        weight=75.0,
        date=datetime.date(2024, 9, 22)
    )
    weight = update_weight_service(db_session, weight_id, weight_data)
    assert weight.id == weight_id
    assert weight.user_id == weights[-1].user_id
    assert weight.weight == 75.0
    assert weight.date == datetime.date(2024, 9, 22)

# Test delete weight
def test_delete_weight(db_session, weights):
    weight_id = weights[-1].id
    delete_weight_service(db_session, weight_id)
    try:
        get_weight_by_id_service(db_session, weight_id)
    except ValueError as e:
        assert str(e) == "Weight not found"
