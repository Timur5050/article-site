# Generated by Django 4.2.1 on 2023-12-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_alter_car_options_car_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
