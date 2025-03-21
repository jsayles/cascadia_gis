from django.contrib import admin
from django.urls import path

from cascadia import views


urlpatterns = [
    path("", views.map_detail, name="home"),
    path("map/<int:pk>", views.map_detail, name="map-detail"),
    path("city/<int:pk>/", views.CitiesDetailView.as_view(), name="city-detail"),
    path("admin/", admin.site.urls),
]
