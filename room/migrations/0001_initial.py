# Generated by Django 4.1.7 on 2023-09-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_number", models.CharField(max_length=250)),
                (
                    "room_type",
                    models.CharField(
                        choices=[
                            ("single", "Single"),
                            ("double", "Double"),
                            ("suite", "Suite"),
                        ],
                        default="single",
                        max_length=20,
                    ),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
                ),
            ],
        ),
    ]
