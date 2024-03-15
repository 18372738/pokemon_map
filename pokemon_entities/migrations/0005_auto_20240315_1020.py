# Generated by Django 3.1.14 on 2024-03-15 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20240305_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 10, 20, 15, 203637)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attak',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 10, 20, 15, 203652)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='endurance',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='protection',
            field=models.IntegerField(default=100),
        ),
    ]
