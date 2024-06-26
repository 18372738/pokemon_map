# Generated by Django 3.1.14 on 2024-04-02 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20240317_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='attak',
            new_name='attack',
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
