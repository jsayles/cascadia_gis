"""Nominatum - Open-source geocoding: https://nominatim.org"""

import logging

from geopy.geocoders import Nominatim

from django.contrib.gis.geos.point import Point

logger = logging.getLogger(__name__)


def coordinates_from_address(address):
    address = address.strip() if address else None
    if address:
        logger.debug(f"Nominatim:  Getting coordinates for address: '{address}'")
        geolocator = Nominatim(user_agent="cascadia.design")
        location = geolocator.geocode(address)
        if location:
            return Point(location.longitude, location.latitude)
