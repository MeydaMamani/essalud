from django.urls import path
from .views import KidsView, AnemiaKidsView, SearchKidsView, NominalAnemia, PrintNominal
from django.contrib.auth.decorators import permission_required, login_required

app_name='follow_up'

urlpatterns = [
    path('', login_required(KidsView.as_view()), name='index_boy'),
    path('search/', SearchKidsView.as_view(), name='search_boy'),
    path('anemia/', login_required(AnemiaKidsView.as_view()), name='index_anemia'),
    path('anemia/searchAnemia/', NominalAnemia.as_view(), name='anemia_search'),
    path('anemia/printNominal/', PrintNominal.as_view(), name='anemia_print'),
]