# Generated by Django 4.2.2 on 2023-08-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0010_alter_source_logo_alter_source_logo_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='logo_height',
            field=models.PositiveIntegerField(default=32),
        ),
        migrations.AlterField(
            model_name='source',
            name='logo_width',
            field=models.PositiveIntegerField(default=32),
        ),
    ]
