# Generated by Django 4.2.2 on 2023-08-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_source_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='logo',
            field=models.ImageField(default='image/source_logos/default_logo.png', upload_to='image/source_logos/'),
        ),
    ]
