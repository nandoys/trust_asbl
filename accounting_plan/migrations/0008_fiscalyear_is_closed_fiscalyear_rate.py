# Generated by Django 4.1.4 on 2022-12-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting_plan", "0007_alter_fiscalyear_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="fiscalyear",
            name="is_closed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="fiscalyear",
            name="rate",
            field=models.IntegerField(default=2100),
            preserve_default=False,
        ),
    ]
