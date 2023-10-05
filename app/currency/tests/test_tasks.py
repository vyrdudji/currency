import pytest
import requests_mock
from app.currency.tasks import parse_monobank
from app.currency.models import Rate, Source


@pytest.mark.django_db
def test_parse_monobank():
    with requests_mock.Mocker() as m:
        m.get('https://api.monobank.ua/bank/currency', json=[
            {'currencyCodeA': 840, 'currencyCodeB': 980, 'rateBuy': 27.2, 'rateSell': 27.6},
            {'currencyCodeA': 978, 'currencyCodeB': 980, 'rateBuy': 31.2, 'rateSell': 31.6},
        ])

        parse_monobank.apply()

        assert Rate.objects.count() == 2
        assert Source.objects.count() == 1

        usd_rate = Rate.objects.get(currency=Rate.RateCurrencyChoices.USD)
        assert usd_rate.buy == 27.2
        assert usd_rate.sell == 27.6

        eur_rate = Rate.objects.get(currency=Rate.RateCurrencyChoices.EUR)
        assert eur_rate.buy == 31.2
        assert eur_rate.sell == 31.6
