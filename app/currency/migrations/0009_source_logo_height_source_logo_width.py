# Generated by Django 4.2.2 on 2023-08-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_alter_source_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='logo_height',
            field=models.PositiveIntegerField(default=32),
        ),
        migrations.AddField(
            model_name='source',
            name='logo_width',
            field=models.PositiveIntegerField(default=32),
        ),
    ]