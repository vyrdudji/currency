# Generated by Django 4.2.2 on 2023-06-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateTimeField()),
                ('currency_type', models.CharField(max_length=3)),
            ],
        ),
    ]
