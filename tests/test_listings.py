from app import create_app
from app.models.listing import Listing
from app.services.listing_service import ListingService
import pytest

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database():
    # Code to initialize the database goes here
    pass

def test_create_listing(client, init_database):
    response = client.post('/listings/', json={
        'title': 'Cozy Cottage',
        'description': 'A cozy cottage in the woods.',
        'price': 100,
        'location': 'Woodland'
    })
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_get_listing(client, init_database):
    response = client.get('/listings/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Cozy Cottage'

def test_update_listing(client, init_database):
    response = client.put('/listings/1', json={
        'title': 'Updated Cozy Cottage',
        'description': 'An updated cozy cottage in the woods.',
        'price': 120,
        'location': 'Woodland'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Updated Cozy Cottage'

def test_delete_listing(client, init_database):
    response = client.delete('/listings/1')
    assert response.status_code == 204

def test_get_all_listings(client, init_database):
    response = client.get('/listings/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Ensure the response is a list of listings