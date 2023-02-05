from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class AvailableCash(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    previouse_balance = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return f'You have a current balance of: GHC {self.amount - self.previouse_balance}'


class Expenditure(models.Model):
    claimed_by = models.CharField(max_length=20, blank=True, null=True)
    purpose_of = models.CharField(max_length=200, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    date_of_claim = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return f"{self.amount} claimed by {self.claimed_by} on {self.date_of_claim}"
