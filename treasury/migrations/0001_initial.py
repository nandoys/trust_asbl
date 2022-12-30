# Generated by Django 4.1.4 on 2022-12-29 13:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("symbol_iso", models.CharField(max_length=3, unique=True)),
                ("country_iso", models.CharField(max_length=3, unique=True)),
                ("is_local", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="CurrencyDailyRate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("rate", models.IntegerField()),
                ("rate_at", models.DateField(auto_now=True, unique=True)),
                ("in_use", models.BooleanField(default=True)),
                (
                    "from_currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_currency",
                        to="treasury.currency",
                    ),
                ),
                (
                    "to_currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_currency",
                        to="treasury.currency",
                    ),
                ),
            ],
        ),
    ]
