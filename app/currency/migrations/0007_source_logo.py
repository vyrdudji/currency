# Generated by Django 4.2.2 on 2023-08-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_rate_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='logo',
            field=models.ImageField(default='default_logo.png', upload_to='image/source_logos/'),
        ),
    ]
