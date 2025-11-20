from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_amenities(client):
    response = client.get('/amenities/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_amenity(client):
    response = client.post('/amenities/', json={'name': 'WiFi'})
    assert response.status_code == 201
    assert response.json['name'] == 'WiFi'

def test_create_amenity_missing_name(client):
    response = client.post('/amenities/', json={})
    assert response.status_code == 400
    assert response.json['message'] == 'Amenity name required'

def test_get_amenities_for_listing(client):
    response = client.get('/listings/1/amenities')
    assert response.status_code == 200
    assert 'listing_id' in response.json
    assert response.json['listing_id'] == 1

def test_get_amenities_for_nonexistent_listing(client):
    response = client.get('/listings/999/amenities')
    assert response.status_code == 404
    assert response.json['message'] == 'Listing not found'