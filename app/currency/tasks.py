import requests
from celery import shared_task
from .consts import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME
from .models import Rate, Source
from .utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    source, _ = Source.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank'
        }
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'
    response = requests.get(url)
    response.raise_for_status()

    rates = response.json()

    available_currencies = {
        'USD': Rate.RateCurrencyChoices.USD,
        'EUR': Rate.RateCurrencyChoices.EUR
    }

    for rate in rates:
        currency_code = rate['ccy']
        if currency_code in available_currencies:
            currency = available_currencies[currency_code]
            buy = to_2_places_decimal(rate['buy'])
            sale = to_2_places_decimal(rate['sale'])

            last_rate = Rate.objects.filter(source=source, currency=currency) \
                .order_by('-created') \
                .first()

            if last_rate is None or last_rate.buy != buy or last_rate.sell != sale:
                Rate.objects.create(
                    buy=buy,
                    sell=sale,
                    source=source,
                    currency=currency
                )


@shared_task
def parse_monobank():
    source, _ = Source.objects.get_or_create(
        code_name=MONOBANK_CODE_NAME,
        defaults={
            'name': 'Monobank'
        }
    )

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()

    rates = response.json()

    available_currencies = {
        840: Rate.RateCurrencyChoices.USD,  # USD
        978: Rate.RateCurrencyChoices.EUR,  # EUR
        348: Rate.RateCurrencyChoices.HUF,  # HUF
        203: Rate.RateCurrencyChoices.CZK,  # CZK
        752: Rate.RateCurrencyChoices.SEK,  # SEK
        826: Rate.RateCurrencyChoices.GBP,  # GBP
        643: Rate.RateCurrencyChoices.RUB,  # RUB
    }

    for rate in rates:
        currency_code = rate['currencyCodeA']
        if currency_code in available_currencies:
            currency = available_currencies[currency_code]
            buy = to_2_places_decimal(rate['rateBuy'])
            sale = to_2_places_decimal(rate['rateSell'])

            last_rate = Rate.objects.filter(source=source, currency=currency) \
                .order_by('-created') \
                .first()

            if last_rate is None or last_rate.buy != buy or last_rate.sell != sale:
                Rate.objects.create(
                    buy=buy,
                    sell=sale,
                    source=source,
                    currency=currency
                )
