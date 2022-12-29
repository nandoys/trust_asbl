# Generated by Django 4.1.4 on 2022-12-28 09:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounting_plan", "0005_budget"),
    ]

    operations = [
        migrations.CreateModel(
            name="FiscalYear",
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
                ("year", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="budget",
            name="fiscal_year",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounting_plan.fiscalyear",
            ),
        ),
    ]