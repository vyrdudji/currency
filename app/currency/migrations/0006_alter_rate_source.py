# Generated by Django 4.2.2 on 2023-08-02 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_requestresponselog_alter_rate_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='currency.source'),
        ),
    ]
