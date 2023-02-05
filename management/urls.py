from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cash', views.cash_, name='cash'),
    path('properties', views.properties, name='property'),
    path('payment', views.payment, name='payment'),
    path('balance', views.balance, name='balance'),
    path('employee', views.employee, name='employment'),
]
