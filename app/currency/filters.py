import django_filters
from .models import Rate, ContactUs, Source


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ['exact', 'icontains', 'gte', 'lte'],
            'sell': ['exact', 'icontains', 'gte', 'lte'],
            'currency': ['exact'],
            'source': ['exact'],
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'email_from': ['icontains'],
            'subject': ['icontains'],
            'message': ['icontains'],
        }


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = {
            'name': ['icontains'],
            'source_url': ['icontains'],
        }
