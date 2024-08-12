from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path
from . import views
from .views import *

app_name='packages'

urlpatterns = [
    path('boys', login_required(FollowKidsView.as_view()), name='boys'),
    path('boys/api/', ListKidsFollow.as_view(), name='list_boys'),
    path('boys/printExcel/', views.PrintPackChild.as_view(), name='print_boys'),
    path('pregnant', login_required(FollowPregnantView.as_view()), name='pregnant'),
    path('pregnant/api/', ListPregnantFollow.as_view(), name='list_pregnant'),
    path('pregnant/printExcel/', views.PrintPackPregnant.as_view(), name='print_pregnant'),
]