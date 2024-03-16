from django.db import models  # noqa F401
from datetime import datetime




class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    previous_evolution = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(default=100)
    attak = models.IntegerField(default=100)
    protection = models.IntegerField(default=100)
    endurance = models.IntegerField(default=100)
