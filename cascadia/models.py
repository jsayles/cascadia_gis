import logging

from django.db import models
from django.contrib.gis.db import models as geomodels
from django.urls import reverse


logger = logging.getLogger(__name__)


class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ("name",)

        # plural form in admin view
        verbose_name_plural = "cities"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("city-detail", kwargs={"pk": self.pk})
    
