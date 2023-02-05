from . import views
from django.urls import path

urlpatterns = [
    path('authenticate', views.login_user, name='login'),
    path('register', views.signup, name='signup'),
    path('signout', views.logout_user, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
