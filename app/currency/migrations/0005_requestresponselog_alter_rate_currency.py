# Generated by Django 4.2.2 on 2023-07-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=10)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'USD - US Dollar'), (2, 'EUR - Euro'), (3, 'HUF - Hungarian Forint'), (4, 'CZK - Czech Koruna'), (5, 'SEK - Swedish Krona'), (6, 'GBP - British Pound'), (7, 'RUB - Russian Ruble')]),
        ),
    ]
