from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import PersonView, searchPerson, CreatePerson
from . import views
from .views import *

app_name="person"

urlpatterns = [
    path('', login_required(PersonView.as_view()), name='index_person'),
    path('searchperson/', searchPerson.as_view(), name='search_person'),
    path('cperson/', CreatePerson.as_view(), name='create_person'),
    path('crudUser/', CrudUser.as_view(), name='crud_red'),
]