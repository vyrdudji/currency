import pytest
from django.urls import reverse
from app.currency.models import Source


# Test Views
@pytest.mark.django_db
def test_source_list_view(api_client):
    Source.objects.create(name='Test Source', source_url='http://test.com')
    url = reverse('source_list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'Test Source' in str(response.content)


@pytest.mark.django_db
def test_source_detail_view(api_client):
    source = Source.objects.create(name='Test Source', source_url='http://test.com')
    url = reverse('source_details', args=[source.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'Test Source' in str(response.content)
