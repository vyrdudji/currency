from PIL import Image
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import os
import re


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
    logo = models.ImageField(
        upload_to='source_logos/',
        default='source_logos/default_logo.png'
    )
    logo_width = models.PositiveIntegerField(default=32)
    logo_height = models.PositiveIntegerField(default=32)

    def save(self, *args, **kwargs):
        media_root = settings.MEDIA_ROOT

        if self.pk:
            original_instance = Source.objects.get(pk=self.pk)

            if original_instance.logo != self.logo:
                # Delete the old logo file
                old_logo_path = os.path.join(media_root, str(original_instance.logo))
                if os.path.exists(old_logo_path):
                    os.remove(old_logo_path)

        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)
        output_size = (self.logo_width, self.logo_height)
        img.thumbnail(output_size)

        img_path = os.path.join(media_root, str(self.logo))

        img.save(img_path)

        original_img_path = os.path.join(media_root, 'source_logos', 'original_' + os.path.basename(img_path))
        self.logo.storage.save(original_img_path, self.logo.storage.open(img_path))

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    time = models.IntegerField()


def clean_phone_number(sender, instance, **kwargs):
    if instance.telephone:
        instance.telephone = re.sub(r'\D', '', instance.telephone)


models.signals.pre_save.connect(clean_phone_number, sender=Source)
