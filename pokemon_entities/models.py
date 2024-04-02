from django.db import models  # noqa F401
from datetime import datetime




class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField('Название (рус.)', max_length=200)
    title_en = models.CharField('Название (анг.)', max_length=200, blank=True)
    title_jp = models.CharField('Название (яп.)', max_length=200, blank=True)
    photo = models.ImageField('Изображение', null=True)
    description = models.TextField('Описнаие', blank=True)
    previous_evolution = models.ForeignKey("self", verbose_name="Прошлая эволюция", on_delete=models.SET_NULL, null=True, related_name="next_evolution")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Характеристика покемона"""
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время появления")
    disappeared_at = models.DateTimeField("Время исчезновения")
    level = models.IntegerField("Уровень", null=True, blank=True)
    health = models.IntegerField("Здоровье", null=True, blank=True)
    attack = models.IntegerField("Атака", null=True, blank=True)
    protection = models.IntegerField("Защита", null=True, blank=True)
    endurance = models.IntegerField("Выносливостьн", null=True, blank=True)

    def __str__(self):
        return self.pokemon.title
