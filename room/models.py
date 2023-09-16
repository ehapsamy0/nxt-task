from django.db import models
from .choices import RoomTypeChoices

# Create your models here.


class Room(models.Model):
    room_number = models.CharField(max_length=250,db_index=True)
    room_type = models.CharField(
        max_length=20, choices=RoomTypeChoices.choices, default=RoomTypeChoices.SINGLE
    )
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)

    def __str__(self) -> str:
        return f"{self.room_number} type {self.room_type}"

    class Meta:
        ordering = ['id']
