from django.views.generic import DetailView
from django.shortcuts import render

from cascadia.models import Map, City


def map_detail(request, pk=None):
    map = Map.objects.get(pk=pk) if pk else Map.objects.first()

    cities = []
    for city in City.objects.filter(geometry__within=map.geometry):
        cities.append(
            {
                "name": city.name,
                "lat": city.geometry.y,
                "lon": city.geometry.x,
                "url": city.get_absolute_url(),
            }
        )

    context = {
        "map": map,
        "cities": cities,
    }
    return render(request, "cascadia/map-detail.html", context)


class CitiesDetailView(DetailView):
    template_name = "cascadia/city-detail.html"
    model = City
