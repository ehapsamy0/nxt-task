"""
handles model choices
"""

from django.db import models


class ReservationStatusChoices(models.TextChoices):

    PENDING = ("pending", "Pending")
    CANCEL = ("cancel", "Cancel")
    EXPIRED = ("expired", "Expired")
