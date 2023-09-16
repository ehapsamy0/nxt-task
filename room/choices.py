"""
handles model choices
"""

from django.db import models


class RoomTypeChoices(models.TextChoices):
    """
    , type (e.g., single, double, suite)
    """

    SINGLE = ("single", "Single")
    DOUBLE = ("double", "Double")
    SUITE = ("suite", "Suite")
