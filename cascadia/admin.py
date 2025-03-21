from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from cascadia.models import Map, City


class LocalGISModelAdmin(GISModelAdmin):
    gis_widget_kwargs = {
        "attrs": {
            "default_lat": 49.2853396,
            "default_lon": -123.1242487,
        }
    }


@admin.register(Map)
class MapAdmin(LocalGISModelAdmin):
    list_display = ["name", "geometry"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(City)
class CityAdmin(LocalGISModelAdmin):
    list_display = ["name", "geometry"]
    search_fields = ["name"]
    ordering = ["name"]
