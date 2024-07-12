from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.core import serializers
from django.http import JsonResponse, HttpResponse, QueryDict
from datetime import datetime
import json

from apps.packages.models import PackChildFollow
from apps.main.models import Provincia, Distrito, Establecimiento


class KidsView(TemplateView):
    template_name = 'kids/index.html'


class AnemiaKidsView(TemplateView):
    template_name = 'anemia/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['provincia'] = Provincia.objects.all()
        return context


class DistrictView(View):
    def get(self, request, *args, **kwargs):
        data = Distrito.objects.filter(parent = request.GET['id'])
        data = serializers.serialize('json', data, fields=['codigo', 'nombre'])
        return HttpResponse(data, content_type='application/json')


class StablishmentView(View):
    def get(self, request, *args, **kwargs):
        data = Establecimiento.objects.filter(parent = request.GET['id'])
        data = serializers.serialize('json', data, fields=['codigo', 'nombre'])
        return HttpResponse(data, content_type='application/json')


class SearchKidsView(View):
    def get(self, request, *args, **kwargs):
        # agreement = PackChildFollow.objects.get(pk=request.PUT['agreement_key'])
        # data_update.agreement.add(agreement)

        data_saved = PackChildFollow.objects.filter(documento=request.GET['doc'])
        format_data = serializers.serialize('json', data_saved, indent=2, use_natural_foreign_keys=True)
        return HttpResponse(format_data, content_type='application/json')