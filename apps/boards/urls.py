from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

app_name="boards"

urlpatterns = [
    path('coverage/', login_required(views.CoverageView.as_view()), name='index_cov'),
    path('coverage/list/', views.ListCoverage.as_view(), name='list_rn'),
    path('coverage/printNominal/', views.PrintNominal.as_view(), name='print_nom'),
]