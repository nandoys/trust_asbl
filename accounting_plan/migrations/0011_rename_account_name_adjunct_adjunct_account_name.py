# Generated by Django 4.1.4 on 2022-12-29 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounting_plan", "0010_adjunct"),
    ]

    operations = [
        migrations.RenameField(
            model_name="adjunct",
            old_name="account_name",
            new_name="adjunct_account_name",
        ),
    ]