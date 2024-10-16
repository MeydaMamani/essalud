from django.urls import path
from .views import *
from django.contrib.auth.decorators import permission_required, login_required

app_name='follow_up'

urlpatterns = [
    path('', login_required(KidsView.as_view()), name='index_boy'),
    path('search/', SearchKidsView.as_view(), name='search_boy'),
    path('anemiaKids/', login_required(AnemiaKidsView.as_view()), name='index_anemia'),
    path('anemiaKids/search/', NominalAnemia.as_view(), name='anemia_search'),
    path('anemiaKids/printNominal/', PrintNomAnem.as_view(), name='anemia_print'),
    path('goals/', login_required(MetasPriorView.as_view()), name='index_goals'),
    path('goals/list/', ListMetasPrior.as_view(), name='goals_list'),
    path('goals/avance/', AdvMetasPriorXAct.as_view(), name='goals_avance'),
    path('goals/printExcel/', PrintGoals.as_view(), name='goals_print'),
    path('inmunization/', login_required(InmunizationView.as_view()), name='index_inmunization'),
    path('inmunization/list/', NominalInmunization.as_view(), name='list_inmunization'),
    path('inmunization/print/', PrintInmunization.as_view(), name='print_inmunization'),
]