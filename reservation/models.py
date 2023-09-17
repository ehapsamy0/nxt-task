from django.db import models
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from django.utils import timezone

# Create your models here.
from .choices import ReservationStatusChoices
from room.models import Room
from .mixins import TimeStampModelMixin

User = get_user_model()


class Reservation(TimeStampModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="created datetime")
    modified = models.DateTimeField(
        auto_now=True, verbose_name="last modified datetime"
    )

    def clean(self):
        # Check if start_date is in the past
        if self.start_date < timezone.now().date():
            raise ValidationError({"message": "Start date cannot be in the past."})

        # Check if end_date is equal to or lower than start_date
        if self.end_date <= self.start_date:
            raise ValidationError({"message": "End date must be after the start date."})

    def save(self, *args, **kwargs):
        self.full_clean()  # Perform clean() before saving
        super().save(*args, **kwargs)


class ReservationStatus(TimeStampModelMixin):
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="reservation_history"
    )
    status = models.CharField(
        max_length=50,
        choices=ReservationStatusChoices.choices,
        default=ReservationStatusChoices.PENDING,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
