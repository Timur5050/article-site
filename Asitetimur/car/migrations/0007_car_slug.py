# Generated by Django 4.2.1 on 2024-01-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_remove_car_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]