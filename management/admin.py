from django.contrib import admin
from .models import AvailableCash
from .models import Expenditure

# Register your models here.


class CashAdmin(admin.ModelAdmin):
    list_display = ('amount', 'previouse_balance', 'date')


admin.site.register(AvailableCash, CashAdmin)


class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('claimed_by', 'purpose_of', 'amount', 'date_of_claim')


admin.site.register(Expenditure, ExpenditureAdmin)
