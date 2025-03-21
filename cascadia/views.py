from django.views.generic import DetailView
from django.shortcuts import render

from cascadia.models import Map, City


def home(request):
    map = Map.objects.first()
    cities = City.objects.all()

    context = {
        "map": map,
        "cities": cities,
    }
    return render(request, "cascadia/home.html", context)


class CitiesDetailView(DetailView):
    template_name = "cascadia/city-detail.html"
    model = City
