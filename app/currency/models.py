from django.db import models
from django.utils.translation import gettext_lazy as _


class Rate(models.Model):
    class RateCurrencyChoices(models.IntegerChoices):
        USD = 1, _('USD - US Dollar')
        EUR = 2, _('EUR - Euro')
        HUF = 3, _('HUF - Hungarian Forint')
        CZK = 4, _('CZK - Czech Koruna')
        SEK = 5, _('SEK - Swedish Krona')
        GBP = 6, _('GBP - British Pound')
        RUB = 7, _('RUB - Russian Ruble')

    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(choices=RateCurrencyChoices.choices)
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email_from


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    telephone = models.CharField(max_length=12)
    address_change = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    time = models.IntegerField()
