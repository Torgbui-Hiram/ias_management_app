from django import forms
from django.utils import timezone
from .models import Expenditure, AvailableCash, Employee_Records


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


# Employment detail form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_Records
        fields = ('first_name', 'midle_name', 'last_name', 'other_name',
                  'date_of_birth', 'appointment_date', 'nationality', 'prove_of_id', 'job_title', 'role')

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['first_name'].label = ''
        # self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer, letters, digit, and @/./+/-/_only.</small></span>'

        self.fields['midle_name'].widget.attrs['class'] = 'form-control'
        self.fields['midle_name'].widget.attrs['placeholder'] = 'Enter midle name'
        self.fields['midle_name'].label = ''
        # self.fields['midle_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer, letters, digit, and @/./+/-/_only.</small></span>'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['last_name'].label = ''
        # self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer, letters, digit, and @/./+/-/_only.</small></span>'

        self.fields['other_name'].widget.attrs['class'] = 'form-control'
        self.fields['other_name'].widget.attrs['placeholder'] = 'Enter other name'
        self.fields['other_name'].label = ''
        # self.fields['other_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer, letters, digit, and @/./+/-/_only.</small></span>'

        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Enter date of birth'
        self.fields['date_of_birth'].label = ''
        # self.fields['date_of_birth'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer, letters, digit, and @/./+/-/_only.</small></span>'

        self.fields['nationality'].widget.attrs['class'] = 'btn btn-dark dropdown-toggle'
        self.fields['nationality'].label = 'Select country'

        self.fields['prove_of_id'].widget.attrs['class'] = 'btn btn-dark dropdown-toggle'
        self.fields['prove_of_id'].label = 'ID type'

        self.fields['job_title'].widget.attrs['class'] = 'btn btn-dark dropdown-toggle'
        self.fields['job_title'].label = 'Job Title'

        self.fields['appointment_date'].widget.attrs['class'] = 'form-control'
        self.fields['appointment_date'].widget.attrs['placeholder'] = 'Enter appointment date'
        self.fields['appointment_date'].label = ''

        self.fields['role'].widget.attrs['class'] = 'btn btn-dark dropdown-toggle'
        self.fields['role'].label = 'Role'
