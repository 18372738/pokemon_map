import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def get_img_url(request, pokemon):
    if not pokemon.photo:
        return DEFAULT_IMAGE_URL
    return request.build_absolute_uri(pokemon.photo.url)


def show_all_pokemons(request):
    now = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    active_pokemons = PokemonEntity.objects.filter(appeared_at__lte=now, disappeared_at__gte=now)
    for pokemon_entity in active_pokemons:
        pokemon_entity_img_url = get_img_url(request, pokemon_entity.pokemon)
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity_img_url,
        )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemon_img_url = get_img_url(request, pokemon)
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon_img_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    now = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(appeared_at__lte=now, disappeared_at__gt=now):
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.photo.url)
        )

    previous_evolution = {}
    if pokemon.previous_evolution:
        previous_evolution = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(pokemon.previous_evolution.photo.url),
        }

    next_pokemon = pokemon.next_evolutions.first()
    next_evolution = {}
    if next_pokemon:
        next_evolution = {
            "title_ru": next_pokemon.title,
            "pokemon_id": next_pokemon.id,
            "img_url": request.build_absolute_uri(next_pokemon.photo.url)
        }

    pokemon_dict = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.photo.url),
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution,
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_dict
    })
