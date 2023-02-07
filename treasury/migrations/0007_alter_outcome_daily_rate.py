# Generated by Django 4.1.4 on 2023-01-19 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("treasury", "0006_alter_income_slip_number_alter_outcome_slip_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outcome",
            name="daily_rate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="treasury.currencydailyrate",
            ),
        ),
    ]