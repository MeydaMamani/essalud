from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

app_name="dashboard"

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', login_required(views.logoutUser), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/', login_required(views.HomeView.as_view()), name='home'),
]