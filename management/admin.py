from django.contrib import admin
from .models import AvailableCash, Expenditure, Job, Employee_Records, Nationality, JobRoles, IdentityCard
from django.contrib.auth.models import User, Group, GroupManager
# Register your models here.


class CashAdmin(admin.ModelAdmin):
    list_display = ('amount', 'previouse_balance', 'date')


admin.site.register(AvailableCash, CashAdmin)


# Expenditure and expensis
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('claimed_by', 'purpose_of', 'amount', 'date_of_claim')


admin.site.register(Expenditure, ExpenditureAdmin)


# Job positions availabe
class JobAdmin(admin.ModelAdmin):
    list_display = ('roles',)


admin.site.register(Job, JobAdmin)


# Employee records and information
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'midle_name', 'last_name', 'other_name', 'nationality',
                    'date_of_birth', 'prove_of_id', 'job_title', 'appointment_date', 'role')


admin.site.register(Employee_Records, EmployeeAdmin)


# Role played by employee
@admin.register(JobRoles)
class JobRolesAdmin(admin.ModelAdmin):
    list_display = ('possition_held',)


@admin.register(IdentityCard)
class IdentityCardAdmin(admin.ModelAdmin):
    list_display = ('id_types',)
