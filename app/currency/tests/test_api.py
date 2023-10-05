import pytest
from rest_framework.test import APIClient
from app.currency.models import Source


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_source(api_client):
    response = api_client.post('/api/source/', {'name': 'Test Source', 'source_url': 'http://test.com'})
    assert response.status_code == 201
    assert Source.objects.count() == 1


@pytest.mark.django_db
def test_read_source(api_client):
    source = Source.objects.create(name='Test Source', source_url='http://test.com')
    response = api_client.get(f'/api/source/{source.id}/')
    assert response.status_code == 200
    assert response.json()['name'] == 'Test Source'


@pytest.mark.django_db
def test_update_source(api_client):
    source = Source.objects.create(name='Test Source', source_url='http://test.com')
    new_data = {'name': 'Updated Source', 'source_url': 'http://updated.com'}
    response = api_client.put(f'/api/source/{source.id}/', new_data, format='json')
    assert response.status_code == 200
    updated_source = Source.objects.get(id=source.id)
    assert updated_source.name == 'Updated Source'
    assert updated_source.source_url == 'http://updated.com'


@pytest.mark.django_db
def test_delete_source(api_client):
    source = Source.objects.create(name='Test Source', source_url='http://test.com')
    response = api_client.delete(f'/api/source/{source.id}/')
    assert response.status_code == 204
    assert Source.objects.count() == 0
