from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3)  # usd, eur
    source = models.CharField(max_length=68)


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


class Rate(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'USD - US Dollar'),
        ('EUR', 'EUR - Euro'),
        ('HUF', 'HUF - Hungarian Forint'),
        ('CZK', 'CZK - Czech Koruna'),
        ('SEK', 'SEK - Swedish Krona'),
        ('GBP', 'GBP - British Pound'),
        ('RUB', 'RUB - Russian Ruble'),
    ]

    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    source = models.CharField(max_length=68)

