from django.views.generic import DetailView
from django.shortcuts import render

from cascadia.models import Map, City


def home(request):
    map = Map.objects.first()

    # cities = City.objects.all()
    vancouver = City.objects.get(id=7256)
    seattle = City.objects.get(id=7109)
    portland = City.objects.get(id=6782)
    cities = [vancouver, seattle, portland]

    context = {
        "map": map,
        "cities": cities,
        "vancouver": vancouver,
        "seattle": seattle,
        "portland": portland,
    }
    return render(request, "cascadia/home.html", context)


class CitiesDetailView(DetailView):
    template_name = "cascadia/city-detail.html"
    model = City
