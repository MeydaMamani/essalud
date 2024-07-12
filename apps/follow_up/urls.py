from django.urls import path
from .views import KidsView, AnemiaKidsView, SearchKidsView, DistrictView, StablishmentView
from django.contrib.auth.decorators import permission_required, login_required

app_name='follow_up'

urlpatterns = [
    path('', login_required(KidsView.as_view()), name='index_red'),
    path('search/', SearchKidsView.as_view(), name='search'),
    path('anemia/', login_required(AnemiaKidsView.as_view()), name='index_red'),
    path('anemia/filterDist/', DistrictView.as_view(), name='filter_dist'),
    path('anemia/filterEess/', StablishmentView.as_view(), name='filter_dist'),
]