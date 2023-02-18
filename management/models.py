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


class Nationality(models.Model):
    countries = models.CharField(max_length=50)

    def __str__(self):
        return self.countries


class Job(models.Model):
    roles = models.CharField(max_length=50)

    def __str__(self):
        return self.roles


class JobRoles(models.Model):
    possition_held = models.CharField(max_length=50)

    def __str__(self):
        return self.possition_held


class IdentityCard(models.Model):
    id_types = models.CharField(max_length=30, blank=True, null=True)


class Employee_Records(models.Model):
    # list of countries
    COUNTRY_LIST = [
        ('Ghana', 'Ghana'),
        ('Togo', 'Togo'),
        ('Nigeria', 'Nigeria'),
        ('Abijan', 'Abijan'),]
    # Type of identification
    ID_TYPES = [
        ('Passport', 'Passport'),
        ('Drivers lincense', 'Drivers lincense'),
        ('Voters ID', 'Voters ID'),
        ('Ghana Card', 'Ghana Card'),
        ('NHIS', 'NHIS'),
        ('SSNIT', 'SSNIT'), ]
    # Job title available
    JOB_ROLES = [
        ('Electrical', 'Electrical'),
        ('Generator', 'Generator'),
        ('Electronics', 'Electronics'),
        ('Pump Technician', 'Pump Technician'),]
    # Positions available
    POSITION = [
        ('Team leader', 'Team leader'),
        ('Technician Assis', 'Technician Assis'),
        ('Security', 'Security'),
        ('Department Manager', 'Department Manager'),
        ('Human Resource', 'Human Resource'), ]

    first_name = models.CharField(max_length=25)
    midle_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25, blank=True, null=True)
    nationality = models.CharField(
        max_length=50, choices=COUNTRY_LIST, blank=True, null=True, default='Ghana')
    date_of_birth = models.DateField(blank=True, null=True)
    prove_of_id = models.CharField(
        max_length=50, choices=ID_TYPES, blank=True, null=True, default='Ghana Card')
    id_number = models.CharField(max_length=30, blank=True, null=True)
    job_title = models.CharField(
        max_length=50, choices=POSITION, blank=True, default="Team leader")
    appointment_date = models.DateField(blank=True, null=True)
    role = models.CharField(
        max_length=50, choices=JOB_ROLES, blank=True, null=True, default='Pump Technician')
