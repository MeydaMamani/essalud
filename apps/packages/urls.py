from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path
from . import views
from .views import *
from .views import FollowKidsView, ListKidsFollow

app_name='packages'

urlpatterns = [
    path('boys', login_required(FollowKidsView.as_view()), name='boys'),
    path('boys/api/', ListKidsFollow.as_view(), name='list_boys'),
    path('boys/printExcel/', views.ReportPackChildExcel.as_view(), name='print_boys'),
    path('pregnant', login_required(FollowPregnantView.as_view()), name='pregnant'),
]