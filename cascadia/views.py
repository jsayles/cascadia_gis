from django.views.generic import DetailView
from .models import City


class CitiesDetailView(DetailView):
    template_name = "cascadia/city-detail.html"
    model = City
