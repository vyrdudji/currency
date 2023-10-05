import pytest
from app.currency.models import Source


# Test Models
@pytest.mark.django_db
def test_create_source_model():
    source = Source.objects.create(name='Test Source', source_url='http://test.com')
    assert Source.objects.count() == 1
    assert source.name == 'Test Source'
    assert source.source_url == 'http://test.com'
