# Generated by Django 4.2.2 on 2023-08-02 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_phone_number_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', "Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")]),
        ),
    ]