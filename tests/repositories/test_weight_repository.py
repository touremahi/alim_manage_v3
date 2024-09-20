import datetime

from app.schemas import WeightCreate
from app.repositories.weight_repository import (
    create_weight,
    get_weight_by_id,
    get_weights,
    get_weights_by_user_id,
    get_weights_by_date,
    update_weight,
    delete_weight
)

# CRUD operations for Weight model
def test_create_weight(db_session, users):
    weight_data = WeightCreate(
        user_id=users[-1].id,
        date=datetime.date(2023, 1, 1),
        weight=70.5
    )
    weight = create_weight(db_session, weight_data)
    assert weight.user_id == weight_data.user_id
    assert weight.date == weight_data.date
    assert weight.weight == weight_data.weight
    assert weight.id is not None

# get_weight_by_id
def test_get_weight_by_id(db_session, weights):
    weight_id = weights[-1].id
    weight = get_weight_by_id(db_session, weight_id)
    assert weight.user_id == weights[-1].user_id
    assert weight.date == weights[-1].date
    assert weight.weight == weights[-1].weight
    assert weight.id == weight_id

# get_weights
def test_get_weights(db_session, weights):
    weights_list = get_weights(db_session)
    assert len(weights_list) == len(weights)
    for weight in weights_list:
        assert weight.id is not None
        assert weight.user_id is not None
        assert weight.date is not None
        assert weight.weight is not None

# get_weight_by_user_id
def test_get_weights_by_user_id(db_session, weights):
    user_id = weights[-1].user_id
    weights = get_weights_by_user_id(db_session, user_id)
    assert len(weights) == len(weights)
    for weight in weights:
        assert weight.user_id == user_id
        assert weight.date is not None
        assert weight.weight is not None

# get_weight_by_date
def test_get_weights_by_date(db_session, weights):
    date = weights[-1].date
    weight = get_weights_by_date(db_session, date)
    assert len(weight) == len(weights)
    for weight in weight:
        assert weight.date == date
        assert weight.weight is not None
        assert weight.user_id is not None
        assert weight.id is not None

# update_weight
def test_update_weight(db_session, weights):
    weight_id = weights[-1].id
    weight_data = WeightCreate(
        user_id=weights[-1].user_id,
        date=weights[-1].date,
        weight=75.0
    )
    weight = update_weight(db_session, weight_id, weight_data)
    assert weight.user_id == weight_data.user_id
    assert weight.date == weight_data.date
    assert weight.weight == weight_data.weight
    assert weight.id == weight_id

# delete_weight
def test_delete_weight(db_session, weights):
    weight_id = weights[-1].id
    delete_weight(db_session, weight_id)
    weight = get_weight_by_id(db_session, weight_id)
    assert weight is None
