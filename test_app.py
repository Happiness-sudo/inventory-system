import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get('/')
    assert res.status_code == 200


def test_add_item(client):
    res = client.post('/items', json={
        "name": "Milk",
        "brand": "Test"
    })
    assert res.status_code == 200


def test_get_items(client):
    res = client.get('/items')
    assert res.status_code == 200


def test_get_one_item(client):
    client.post('/items', json={"name": "Milk", "brand": "Test"})
    res = client.get('/items/1')
    assert res.status_code == 200


def test_update_item(client):
    client.post('/items', json={"name": "Milk", "brand": "Test"})
    res = client.patch('/items/1', json={"name": "Updated"})
    assert res.status_code == 200


def test_delete_item(client):
    client.post('/items', json={"name": "Milk", "brand": "Test"})
    res = client.delete('/items/1')
    assert res.status_code == 200