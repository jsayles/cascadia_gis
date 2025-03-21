from django.views.generic import DetailView
from django.shortcuts import render

from cascadia.models import Map, City


def home(request):
    map = Map.objects.first()

    # Hardcode cities for now.  Should be a query to get all cities within map boundary.
    # cities = City.objects.all()
    vancouver = City.objects.get(id=7256)
    seattle = City.objects.get(id=7109)
    portland = City.objects.get(id=6782)
    cities = []
    for city in [vancouver, seattle, portland]:
        cities.append(
            {
                "name": city.name,
                "lat": city.geometry.y,
                "lon": city.geometry.x,
                "url": city.get_absolute_url(),
            }
        )

    json_context = {
        "center": [map.geometry.centroid.y, map.geometry.centroid.x],
        "boundary": map.geometry.boundary.geojson,
        "cities": cities,
    }
    context = {
        "map": map,
        "json_context": json_context,
    }
    return render(request, "cascadia/home.html", context)


class CitiesDetailView(DetailView):
    template_name = "cascadia/city-detail.html"
    model = City
