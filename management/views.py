from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AvailableCash, Expenditure, Employee_Records
from .forms import ExpenditureForm, CashForm, EmployeeForm

# Create your views here.


def index(request):
    cash = AvailableCash.objects.all()
    return render(request, 'base.html', {'cash': cash})


def cash_(request):
    if request.method == "POST":
        form = CashForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your cash has been added successfully')
            return redirect('home')
        else:
            messages.success(
                request, 'Please there was a problem adding cash to totals! try again')
            return redirect('cash')
    else:
        form = CashForm(request.POST)
    return render(request, 'cash_available.html', {'form': form})


def properties(request):
    return render(request, 'property.html')


def payment(request):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form = ExpenditureForm()
    return render(request, 'payment.html', {'form': form})


def balance(request):
    amount = AvailableCash.objects.all()
    return render(request, 'balance.html', {'amount': amount})


# Display employee data and information
def employee(request):
    records = Employee_Records.objects.all()
    return render(request, 'employment.html', {'records': records})


# Form to register an employee
def employment_form(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Employee data stored succesfully')
            form.save()
        else:
            messages.success(
                request, 'Sorry! there was an error with your form, try again')
    else:
        form = EmployeeForm()
    return render(request, 'employmentform.html', {'form': form})
