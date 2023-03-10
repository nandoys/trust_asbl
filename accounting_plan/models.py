from django.db import models
from django.db.models.query import Q
import uuid


# Create your models here.
class Main(models.Model):
    types = [('encaissement', 'encaissement'), ('decaissement', 'decaissement')]
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    account_number = models.CharField(max_length=255, unique=True)
    account_name = models.CharField(max_length=255, unique=True)
    account_type = models.CharField(max_length=255, choices=types)
    account_description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.account_name


class Additional(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    account_number = models.CharField(max_length=255, unique=True)
    account_name = models.CharField(max_length=255, unique=True)
    account_description = models.TextField(max_length=500, null=True, blank=True)
    account_main = models.ForeignKey(Main, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_name


class Adjunct(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    account_additional = models.ForeignKey(Additional, on_delete=models.CASCADE)
    adjunct_account_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.adjunct_account_name


class FiscalYear(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    year = models.IntegerField(unique=True)
    rate = models.IntegerField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.year)


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    accounting = models.ForeignKey(Additional, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    plan_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.accounting.account_name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['accounting', 'plan_at'], name='unique_budget'),
        ]


class Monitoring(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    accounting = models.ForeignKey(Additional, on_delete=models.CASCADE)
    warn_at = models.FloatField()
    year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)
    message = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['accounting', 'year'], name='unique_alert'),
        ]
