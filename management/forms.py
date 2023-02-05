from django import forms
from django.utils import timezone
from .models import Expenditure, AvailableCash


# Payment and expensis made
class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ('claimed_by', 'purpose_of', 'amount',)


# Cash given form
class CashForm(forms.ModelForm):
    class Meta:
        model = AvailableCash
        fields = ('amount', 'previouse_balance',)
