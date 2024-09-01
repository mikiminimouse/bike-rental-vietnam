# Generated by Django 5.1 on 2024-09-01 13:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tours", "0004_remove_tour_ship_tour_ship"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour",
            name="ship",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tours.ship",
            ),
        ),
        migrations.CreateModel(
            name="Order",
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
                ("passengers", models.TextField()),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("email_of_initiator", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=50)),
                ("messenger", models.CharField(max_length=50)),
                (
                    "cost_per_person",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("cost_of_tour", models.DecimalField(decimal_places=2, max_digits=10)),
                ("name_of_tour", models.TextField()),
                ("duration_of_tour", models.DurationField()),
                ("status", models.BooleanField(default=False)),
                (
                    "tour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tours.tour"
                    ),
                ),
            ],
        ),
    ]
