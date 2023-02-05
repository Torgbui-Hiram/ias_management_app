from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AvailableCash, Expenditure
from .forms import ExpenditureForm, CashForm

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
    return render(request, 'balance.html')


def employee(request):
    return render(request, 'employment.html')
