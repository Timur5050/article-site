# Generated by Django 4.2.1 on 2024-01-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_car_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
