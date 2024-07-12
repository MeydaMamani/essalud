from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse, QueryDict
from django.core import serializers

from apps.boards.models import Coverage, metaCoverage
from apps.main.models import Provincia, Distrito, Establecimiento

from django.db.models import Sum, F, FloatField
from django.db.models.functions import Cast
from django.db import connection
from datetime import date, datetime

import datetime
import json
import locale

# library excel
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side, Color


# Create your views here.
class CoverageView(TemplateView):
    template_name = 'coverage/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['provincia'] = Provincia.objects.all()
        return context


class ListCoverage(TemplateView):
    def get(self, request, *args, **kwargs):
        dataList = []
        today = date.today()

        if request.GET['red'] == 'TODOS':
            metarn = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('rn'))
            metaLessyear = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('less_1year'))
            metaOneyear = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('one_year'))
            metaFouryear = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('four_year'))
            metaVphGirl = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('girl9_13'))
            metaVphBoy = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('boy9_13'))
            metaGest = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('pregnant'))
            metaInfAdult = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('adult60'))
            metaNeumoAdult = metaCoverage.objects.filter(anio=today.year).aggregate(total=Sum('adult30'))

            bcg = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalBcg=Sum('bcg'), av_bcg=Sum('bcg', output_field=FloatField()) / Cast(metarn['total'], FloatField()) * 100)
            hvb = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalHvb=Sum('hvb'), av_hvb=Sum('hvb', output_field=FloatField()) / Cast(metarn['total'], FloatField()) * 100)
            rota = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalRota=Sum('rota2'), av_rota=Sum('rota2', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            apo = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo=Sum('apo3'), av_apo=Sum('apo3', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            penta = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalPenta=Sum('penta3'), av_penta=Sum('penta3', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            infl2 = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalInfl2=Sum('infl2'), av_infl2=Sum('infl2', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            neumo3 = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalNeumo3=Sum('neumo3'), av_neumo3=Sum('neumo3', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            var = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalVar=Sum('varicela1'), av_var=Sum('varicela1', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            spr1 = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr1=Sum('spr1'), av_spr1=Sum('spr1', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            ama = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalAma=Sum('ama'), av_ama=Sum('ama', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            hav = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalHav=Sum('hav'), av_hav=Sum('hav', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            spr2 = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr2=Sum('spr2'), av_spr2=Sum('spr2', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            dpt2_ref = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalDpt2=Sum('dpt2_ref'), av_dpt2=Sum('dpt2_ref', output_field=FloatField()) / Cast(metaFouryear['total'], FloatField()) * 100)
            apo2_ref = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('apo2_ref'), av_apo2=Sum('apo2_ref', output_field=FloatField()) / Cast(metaFouryear['total'], FloatField()) * 100)
            vph_girl = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalGirl=Sum('vph_girl'), av_girl=Sum('vph_girl', output_field=FloatField()) / Cast(metaVphGirl['total'], FloatField()) * 100)
            vph_boy = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalBoy=Sum('vph_boy'), av_boy=Sum('vph_boy', output_field=FloatField()) / Cast(metaVphBoy['total'], FloatField()) * 100)
            gestante = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalDpta=Sum('dpta'), av_gest=Sum('dpta', output_field=FloatField()) / Cast(metaGest['total'], FloatField()) * 100)
            infAdult = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalInflAdult=Sum('infl_adult'), av_infAdul=Sum('infl_adult', output_field=FloatField()) / Cast(metaInfAdult['total'], FloatField()) * 100)
            neumoAdult = Coverage.objects.filter(anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalNeumoAdult=Sum('neumo_adult'), av_NeumoAdul=Sum('neumo_adult', output_field=FloatField()) / Cast(metaNeumoAdult['total'], FloatField()) * 100)

            resulTotal = {
                'av_bcg': bcg['av_bcg'], 'av_hvb': hvb['av_hvb'], 'av_rota': rota['av_rota'],
                'av_apo': apo['av_apo'], 'av_penta': penta['av_penta'], 'av_infl2': infl2['av_infl2'],
                'av_neumo3': neumo3['av_neumo3'], 'av_var': var['av_var'], 'av_spr1': spr1['av_spr1'],
                'av_ama': ama['av_ama'], 'av_hav': hav['av_hav'], 'av_spr2': spr2['av_spr2'], 'av_dpt2': dpt2_ref['av_dpt2'],
                'av_apo2': apo2_ref['av_apo2'], 'av_girl': vph_girl['av_girl'], 'av_boy': vph_boy['av_boy'],
                'av_gest': gestante['av_gest'], 'av_infAdul': infAdult['av_infAdul'], 'av_NeumoAdul': neumoAdult['av_NeumoAdul'],
            }

        elif request.GET['red'] != 'TODOS' and request.GET['dist'] == 'TODOS':
            metarn = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('rn'))
            metaLessyear = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('less_1year'))
            metaOneyear = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('one_year'))
            metaFouryear = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('four_year'))
            metaVphGirl = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('girl9_13'))
            metaVphBoy = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('boy9_13'))
            metaGest = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('pregnant'))
            metaInfAdult = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('adult60'))
            metaNeumoAdult = metaCoverage.objects.filter(cod_prov=request.GET['red'], anio=today.year).aggregate(total=Sum('adult30'))

            bcg = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalBcg=Sum('bcg'), av_bcg=Sum('bcg', output_field=FloatField()) / Cast(metarn['total'], FloatField()) * 100)
            hvb = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalHvb=Sum('hvb'), av_hvb=Sum('hvb', output_field=FloatField()) / Cast(metarn['total'], FloatField()) * 100)
            rota = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalRota=Sum('rota2'), av_rota=Sum('rota2', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            apo = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo=Sum('apo3'), av_apo=Sum('apo3', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            penta = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalPenta=Sum('penta3'), av_penta=Sum('penta3', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            infl2 = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalInfl2=Sum('infl2'), av_infl2=Sum('infl2', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            neumo3 = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalNeumo3=Sum('neumo3'), av_neumo3=Sum('neumo3', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            var = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalVar=Sum('varicela1'), av_var=Sum('varicela1', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            spr1 = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr1=Sum('spr1'), av_spr1=Sum('spr1', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            ama = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalAma=Sum('ama'), av_ama=Sum('ama', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            hav = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalHav=Sum('hav'), av_hav=Sum('hav', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            spr2 = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr2=Sum('spr2'), av_spr2=Sum('spr2', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            dpt2_ref = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalDpt2=Sum('dpt2_ref'), av_dpt2=Sum('dpt2_ref', output_field=FloatField()) / Cast(metaFouryear['total'], FloatField()) * 100)
            apo2_ref = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('apo2_ref'), av_apo2=Sum('apo2_ref', output_field=FloatField()) / Cast(metaFouryear['total'], FloatField()) * 100)
            vph_girl = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalGirl=Sum('vph_girl'), av_girl=Sum('vph_girl', output_field=FloatField()) / Cast(metaVphGirl['total'], FloatField()) * 100)
            vph_boy = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalBoy=Sum('vph_boy'), av_boy=Sum('vph_boy', output_field=FloatField()) / Cast(metaVphBoy['total'], FloatField()) * 100)
            gestante = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalDpta=Sum('dpta'), av_gest=Sum('dpta', output_field=FloatField()) / Cast(metaGest['total'], FloatField()) * 100)
            infAdult = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalInfAdult=Sum('infl_adult'), av_infAdul=Sum('infl_adult', output_field=FloatField()) / Cast(metaInfAdult['total'], FloatField()) * 100)
            neumoAdult = Coverage.objects.filter(cod_prov=request.GET['red'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalNeumoAdult=Sum('neumo_adult'), av_NeumoAdul=Sum('neumo_adult', output_field=FloatField()) / Cast(metaNeumoAdult['total'], FloatField()) * 100)

            resulTotal = {
                'av_bcg': bcg['av_bcg'], 'av_hvb': hvb['av_hvb'], 'av_rota': rota['av_rota'],
                'av_apo': apo['av_apo'], 'av_penta': penta['av_penta'], 'av_infl2': infl2['av_infl2'],
                'av_neumo3': neumo3['av_neumo3'], 'av_var': var['av_var'], 'av_spr1': spr1['av_spr1'],
                'av_ama': ama['av_ama'], 'av_hav': hav['av_hav'], 'av_spr2': spr2['av_spr2'], 'av_dpt2': dpt2_ref['av_dpt2'],
                'av_apo2': apo2_ref['av_apo2'], 'av_girl': vph_girl['av_girl'], 'av_boy': vph_boy['av_boy'],
                'av_gest': gestante['av_gest'], 'av_infAdul': infAdult['av_infAdul'], 'av_NeumoAdul': neumoAdult['av_NeumoAdul'],
            }

        elif request.GET['dist'] != 'TODOS':
            metarn = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('rn'))
            metaLessyear = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('less_1year'))
            metaOneyear = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('one_year'))
            metaFouryear = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('four_year'))
            metaVphGirl = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('girl9_13'))
            metaVphBoy = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('boy9_13'))
            metaGest = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('pregnant'))
            metaInfAdult = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('adult60'))
            metaNeumoAdult = metaCoverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year).aggregate(total=Sum('adult30'))

            bcg = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalBcg=Sum('bcg'), av_bcg=Sum('bcg', output_field=FloatField()) / Cast(metarn['total'], FloatField()) * 100)
            hvb = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalHvb=Sum('hvb'), av_hvb=Sum('hvb', output_field=FloatField()) / Cast(metarn['total'], FloatField()) * 100)
            rota = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalRota=Sum('rota2'), av_rota=Sum('rota2', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            apo = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo=Sum('apo3'), av_apo=Sum('apo3', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            penta = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalPenta=Sum('penta3'), av_penta=Sum('penta3', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            infl2 = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr1=Sum('infl2'), av_infl2=Sum('infl2', output_field=FloatField()) / Cast(metaLessyear['total'], FloatField()) * 100)
            neumo3 = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalNeumo3=Sum('neumo3'), av_neumo3=Sum('neumo3', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            var = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalVar=Sum('varicela1'), av_var=Sum('varicela1', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            spr1 = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr1=Sum('spr1'), av_spr1=Sum('spr1', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            ama = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalAma=Sum('ama'), av_ama=Sum('ama', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            hav = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalHav=Sum('hav'), av_hav=Sum('hav', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            spr2 = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalSpr2=Sum('spr2'), av_spr2=Sum('spr2', output_field=FloatField()) / Cast(metaOneyear['total'], FloatField()) * 100)
            dpt2_ref = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalDpt2=Sum('dpt2_ref'), av_dpt2=Sum('dpt2_ref', output_field=FloatField()) / Cast(metaFouryear['total'], FloatField()) * 100)
            apo2_ref = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('apo2_ref'), av_apo2=Sum('apo2_ref', output_field=FloatField()) / Cast(metaFouryear['total'], FloatField()) * 100)
            vph_girl = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('vph_girl'), av_girl=Sum('vph_girl', output_field=FloatField()) / Cast(metaVphGirl['total'], FloatField()) * 100)
            vph_boy = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('vph_boy'), av_boy=Sum('vph_boy', output_field=FloatField()) / Cast(metaVphBoy['total'], FloatField()) * 100)
            gestante = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('dpta'), av_gest=Sum('dpta', output_field=FloatField()) / Cast(metaGest['total'], FloatField()) * 100)
            infAdult = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('infl_adult'), av_infAdul=Sum('infl_adult', output_field=FloatField()) / Cast(metaInfAdult['total'], FloatField()) * 100)
            neumoAdult = Coverage.objects.filter(cod_dist=request.GET['dist'], anio=today.year, mes__range=[1, request.GET['month']]).aggregate(totalApo2=Sum('neumo_adult'), av_NeumoAdul=Sum('neumo_adult', output_field=FloatField()) / Cast(metaNeumoAdult['total'], FloatField()) * 100)

            resulTotal = {
                'av_bcg': bcg['av_bcg'], 'av_hvb': hvb['av_hvb'], 'av_rota': rota['av_rota'],
                'av_apo': apo['av_apo'], 'av_penta': penta['av_penta'], 'av_infl2': infl2['av_infl2'],
                'av_neumo3': neumo3['av_neumo3'], 'av_var': var['av_var'], 'av_spr1': spr1['av_spr1'],
                'av_ama': ama['av_ama'], 'av_hav': hav['av_hav'], 'av_spr2': spr2['av_spr2'], 'av_dpt2': dpt2_ref['av_dpt2'],
                'av_apo2': apo2_ref['av_apo2'], 'av_girl': vph_girl['av_girl'], 'av_boy': vph_boy['av_boy'],
                'av_gest': gestante['av_gest'], 'av_infAdul': infAdult['av_infAdul'], 'av_NeumoAdul': neumoAdult['av_NeumoAdul'],
            }

        dataList.extend([resulTotal])

        return HttpResponse(json.dumps(dataList), content_type='application/json')


class DistrictView(View):
    def get(self, request, *args, **kwargs):
        data = Distrito.objects.filter(parent = request.GET['id'])
        data = serializers.serialize('json', data, fields=['codigo', 'nombre'])
        return HttpResponse(data, content_type='application/json')


class PrintNominal(TemplateView):
    def get(self, request, *args, **kwargs):
        locale.setlocale(locale.LC_TIME, 'es_ES')
        nameMonth = datetime.date(1900, int(request.GET['mes']), 1).strftime('%B')

        wb = Workbook()
        ws = wb.active

        def set_border(self, ws, cell_range, types, colors):
            thin = Side(border_style=types, color=colors)
            for row in ws[cell_range]:
                for cell in row:
                    cell.border = Border(top=thin, left=thin, right=thin, bottom=thin)

        set_border(self, ws, "A2:AX2", "medium", "57267C")
        set_border(self, ws, "A4:AX4", "medium", "366092")
        set_border(self, ws, "A6:AX6", "medium", "D9D9D9")

        img = Image('static/img/logoPrint.png')
        ws.add_image(img, 'A2')

        ws.merge_cells('B2:AX2')
        ws.row_dimensions[2].height = 23

        ws.column_dimensions['A'].width = 6
        ws.column_dimensions['B'].width = 14
        ws.column_dimensions['C'].width = 33

        ws['B2'].font = Font(name='Aptos Narrow', size=11, bold=True, color='57267C')
        ws['B2'].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        ws['B2'] = 'ESSALUD PASCO: COBERTURAS DE VACUNACIÓN - ENERO A ' + str(nameMonth).upper() + ' ' + str((date.today()).year)

        ws.merge_cells('A4:AX4')
        ws['A4'].font = Font(name='Aptos Narrow', size=9, bold=True, color='305496')
        ws['A4'] = 'CODIFICACION: HVB: 90744   -   BCG: 90585'

        ws.merge_cells('A6:AX6')
        ws['A6'].font = Font(name='Aptos Narrow', size=9, bold=True, color='757171')
        ws['A6'] = 'Fuente: BD HisMinsa con Fecha: ' + date.today().strftime('%Y-%m-%d') + ' a las 08:30 horas'

        ws.merge_cells('A8:A9')
        ws['A8'] = '#'
        ws['A8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['A8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['A8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')

        ws.merge_cells('B8:B9')
        ws['B8'] = 'Provincia'
        ws['B8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['B8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['B8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')

        ws.merge_cells('C8:C9')
        ws['C8'] = 'Distrito'
        ws['C8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['C8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['C8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')

        ws.merge_cells('D8:D9')
        ws['D8'] = 'Meta'
        ws['D8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['D8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['D8'].fill = PatternFill(start_color='F5F3CB', end_color='F5F3CB', fill_type='solid')

        ws.merge_cells('E8:H8')
        ws['E8'] = 'Recien Nacidos'
        ws['E8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['E8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['E8'].fill = PatternFill(start_color='F5F3CB', end_color='F5F3CB', fill_type='solid')
        ws['E9'] = 'BCG'
        ws['E9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['E9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['E9'].fill = PatternFill(start_color='F5F3CB', end_color='F5F3CB', fill_type='solid')
        ws['F9'] = '%'
        ws['F9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['F9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['F9'].fill = PatternFill(start_color='F5F3CB', end_color='F5F3CB', fill_type='solid')
        ws['G9'] = 'HVB'
        ws['G9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['G9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['G9'].fill = PatternFill(start_color='F5F3CB', end_color='F5F3CB', fill_type='solid')
        ws['H9'] = '%'
        ws['H9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['H9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['H9'].fill = PatternFill(start_color='F5F3CB', end_color='F5F3CB', fill_type='solid')

        ws.merge_cells('I8:I9')
        ws['I8'] = 'Meta'
        ws['I8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['I8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['I8'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')

        ws.merge_cells('J8:Q8')
        ws['J8'] = 'Menores de 1 Año'
        ws['J8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['J8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['J8'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['J9'] = 'Rotavirus'
        ws['J9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['J9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['J9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['K9'] = '%'
        ws['K9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['K9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['K9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['L9'] = 'Polio'
        ws['L9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['L9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['L9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['M9'] = '%'
        ws['M9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['M9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['M9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['N9'] = 'Penta'
        ws['N9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['N9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['N9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['O9'] = '%'
        ws['O9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['O9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['O9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['P9'] = 'Influenza'
        ws['P9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['P9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['P9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')
        ws['Q9'] = '%'
        ws['Q9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['Q9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['Q9'].fill = PatternFill(start_color='F9D3B9', end_color='F9D3B9', fill_type='solid')

        ws.merge_cells('R8:R9')
        ws['R8'] = 'Meta'
        ws['R8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['R8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['R8'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')

        ws.merge_cells('S8:AD8')
        ws['S8'] = 'Niños de 1 Año'
        ws['S8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['S8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['S8'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['S9'] = 'Neumo'
        ws['S9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['S9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['S9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['T9'] = '%'
        ws['T9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['T9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['T9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['U9'] = 'Varicela'
        ws['U9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['U9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['U9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['V9'] = '%'
        ws['V9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['V9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['V9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['W9'] = 'SPR1'
        ws['W9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['W9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['W9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['X9'] = '%'
        ws['X9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['X9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['X9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['Y9'] = 'AMA'
        ws['Y9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['Y9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['Y9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['Z9'] = '%'
        ws['Z9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['Z9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['Z9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['AA9'] = 'Hepatitis'
        ws['AA9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AA9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AA9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['AB9'] = '%'
        ws['AB9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AB9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AB9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['AC9'] = 'SPR2 '
        ws['AC9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AC9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AC9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')
        ws['AD9'] = '%'
        ws['AD9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AD9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AD9'].fill = PatternFill(start_color='F9D5FB', end_color='F9D5FB', fill_type='solid')

        ws.merge_cells('AE8:AE9')
        ws['AE8'] = 'Meta'
        ws['AE8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AE8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AE8'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')

        ws.merge_cells('AF8:AI8')
        ws['AF8'] = 'Niños de 4 Años'
        ws['AF8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AF8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AF8'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
        ws['AF9'] = 'DPT2'
        ws['AF9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AF9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AF9'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
        ws['AG9'] = '%'
        ws['AG9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AG9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AG9'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
        ws['AH9'] = 'APO2'
        ws['AH9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AH9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AH9'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
        ws['AI9'] = '%'
        ws['AI9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AI9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AI9'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')

        ws.merge_cells('AJ8:AO8')
        ws['AJ8'] = 'Niños y Niñas de 9 a 13 Años'
        ws['AJ8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AJ8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AJ8'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')
        ws['AJ9'] = 'Meta'
        ws['AJ9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AJ9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AJ9'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')
        ws['AK9'] = 'VPH Niñas'
        ws['AK9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AK9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AK9'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')
        ws['AL9'] = '%'
        ws['AL9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AL9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AL9'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')
        ws['AM9'] = 'Meta'
        ws['AM9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AM9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AM9'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')
        ws['AN9'] = 'VPH Niños'
        ws['AN9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AN9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AN9'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')
        ws['AO9'] = '%'
        ws['AO9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AO9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AO9'].fill = PatternFill(start_color='DBCAF4', end_color='DBCAF4', fill_type='solid')

        ws.merge_cells('AP8:AP9')
        ws['AP8'] = 'Meta'
        ws['AP8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AP8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AP8'].fill = PatternFill(start_color='B3F5C2', end_color='B3F5C2', fill_type='solid')

        ws.merge_cells('AQ8:AR8')
        ws['AQ8'] = 'Gestantes'
        ws['AQ8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AQ8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AQ8'].fill = PatternFill(start_color='B3F5C2', end_color='B3F5C2', fill_type='solid')
        ws['AQ9'] = 'DPTA'
        ws['AQ9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AQ9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AQ9'].fill = PatternFill(start_color='B3F5C2', end_color='B3F5C2', fill_type='solid')
        ws['AR9'] = '%'
        ws['AR9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AR9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AR9'].fill = PatternFill(start_color='B3F5C2', end_color='B3F5C2', fill_type='solid')

        ws.merge_cells('AS8:AX8')
        ws['AS8'] = 'Adulto Mayor'
        ws['AS8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AS8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AS8'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
        ws['AS9'] = 'Meta'
        ws['AS9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AS9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AS9'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
        ws['AT9'] = 'Influenza'
        ws['AT9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AT9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AT9'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
        ws['AU9'] = '%'
        ws['AU9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AU9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AU9'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
        ws['AV9'] = 'Meta'
        ws['AV9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AV9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AV9'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
        ws['AW9'] = 'Neumococo'
        ws['AW9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AW9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AW9'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
        ws['AX9'] = '%'
        ws['AX9'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['AX9'].alignment = Alignment(horizontal="center", vertical="center")
        ws['AX9'].fill = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')

        c = connection.cursor()
        if request.GET['red'] == 'TODOS':
            c.execute("""SELECT cod_prov, provincia, cod_dist, distrito, SUM(bcg) bcg, SUM(hvb) hvb, SUM(rota2) rota2, SUM(apo3) apo3, SUM(penta3) penta3,
                        SUM(infl2) infl2, sum(neumo3) neumo3, sum(varicela1) varicel, sum(spr1) spr1, sum(ama) ama, sum(hav) hav, sum(spr2) spr2,
                        sum(dpt2_ref) dpt2_ref, sum(apo2_ref) apo2_ref, sum(vph_girl) vph_girl, sum(vph_boy) vph_boy, sum(dpta) dpta,
                        sum(infl_adult) infl_adult, sum(neumo_adult) neumo_adult
                        INTO ESSALUD.dbo.printCobertNominal
                        FROM ESSALUD.dbo.boards_coverage WHERE Anio=2024 and (Mes BETWEEN 1 and 7)
                        AND provincia IS NOT NULL
                        GROUP BY cod_prov, provincia, cod_dist, distrito
                        ORDER BY cod_prov, provincia, cod_dist, distrito""")

        elif request.GET['red'] != 'TODOS' and request.GET['dist'] == 'TODOS':
            c.execute("""SELECT cod_prov, provincia, cod_dist, distrito, SUM(bcg) bcg, SUM(hvb) hvb, SUM(rota2) rota2, SUM(apo3) apo3, SUM(penta3) penta3,
                        SUM(infl2) infl2, sum(neumo3) neumo3, sum(varicela1) varicel, sum(spr1) spr1, sum(ama) ama, sum(hav) hav, sum(spr2) spr2,
                        sum(dpt2_ref) dpt2_ref, sum(apo2_ref) apo2_ref, sum(vph_girl) vph_girl, sum(vph_boy) vph_boy, sum(dpta) dpta,
                        sum(infl_adult) infl_adult, sum(neumo_adult) neumo_adult
                        INTO ESSALUD.dbo.printCobertNominal
                        FROM ESSALUD.dbo.boards_coverage WHERE Anio=2024 and (Mes BETWEEN 1 and 7) and cod_prov=%s
                        AND provincia IS NOT NULL
                        GROUP BY cod_prov, provincia, cod_dist, distrito
                        ORDER BY cod_prov, provincia, cod_dist, distrito""" % (request.GET['red']))

        else:
            c.execute("""SELECT cod_prov, provincia, cod_dist, distrito, SUM(bcg) bcg, SUM(hvb) hvb, SUM(rota2) rota2, SUM(apo3) apo3, SUM(penta3) penta3,
                        SUM(infl2) infl2, sum(neumo3) neumo3, sum(varicela1) varicel, sum(spr1) spr1, sum(ama) ama, sum(hav) hav, sum(spr2) spr2,
                        sum(dpt2_ref) dpt2_ref, sum(apo2_ref) apo2_ref, sum(vph_girl) vph_girl, sum(vph_boy) vph_boy, sum(dpta) dpta,
                        sum(infl_adult) infl_adult, sum(neumo_adult) neumo_adult
                        INTO ESSALUD.dbo.printCobertNominal
                        FROM ESSALUD.dbo.boards_coverage WHERE Anio=2024 and (Mes BETWEEN 1 and 7) and cod_prov=%s and cod_dist=%s
                        AND provincia IS NOT NULL
                        GROUP BY cod_prov, provincia, cod_dist, distrito
                        ORDER BY cod_prov, provincia, cod_dist, distrito""" % (request.GET['red'], request.GET['dist']))

        c.execute("""SELECT B.provincia, B.distrito, SUM(B.rn) meta_rn, iif(A.bcg is null, 0, a.bcg) tot_bcg, iif(A.hvb is null, 0, a.hvb) tot_hvb,
                    round(cast(iif(A.bcg is null, 0, a.bcg) as float)/cast(SUM(B.rn) as float) * 100,1) av_bcg,
                        round(cast(iif(A.hvb is null, 0, a.hvb) as float)/cast(SUM(B.rn) as float) * 100,1) av_hvb,
                        SUM(B.less_1year) meta_lessyear, iif(A.rota2 is null, 0, a.rota2) tot_rota2, iif(A.apo3 is null, 0, a.apo3) tot_apo3,
                        iif(A.penta3 is null, 0, a.penta3) tot_penta3, iif(A.infl2 is null, 0, a.infl2) tot_infl2,
                        round(cast(iif(A.rota2 is null, 0, a.rota2) as float)/cast(SUM(B.less_1year) as float) * 100,1) av_rota2,
                        round(cast(iif(A.apo3 is null, 0, a.apo3) as float)/cast(SUM(B.less_1year) as float) * 100,1) av_apo3,
                        round(cast(iif(A.penta3 is null, 0, a.penta3) as float)/cast(SUM(B.less_1year) as float) * 100,1) av_penta3,
                        round(cast(iif(A.infl2 is null, 0, a.infl2) as float)/cast(SUM(B.less_1year) as float) * 100,1) av_infl2,
                        SUM(B.one_year) meta_oneyear, iif(A.neumo3 is null, 0, a.neumo3) tot_neumo3, iif(A.varicel is null, 0, a.varicel) tot_varicel,
                        iif(A.spr1 is null, 0, a.spr1) tot_spr1, iif(A.ama is null, 0, a.ama) tot_ama, iif(A.hav is null, 0, a.hav) tot_hav,
                        iif(A.spr2 is null, 0, a.spr2) tot_spr2, round(cast(iif(A.neumo3 is null, 0, a.neumo3) as float)/cast(SUM(B.one_year) as float) * 100,1) av_neumo3,
                        round(cast(iif(A.varicel is null, 0, a.varicel) as float)/cast(SUM(B.one_year) as float) * 100,1) av_varicel,
                        round(cast(iif(A.spr1 is null, 0, a.spr1) as float)/cast(SUM(B.one_year) as float) * 100,1) av_spr1,
                        round(cast(iif(A.ama is null, 0, a.ama) as float)/cast(SUM(B.one_year) as float) * 100,1) av_ama,
                        round(cast(iif(A.hav is null, 0, a.hav) as float)/cast(SUM(B.one_year) as float) * 100,1) av_hav,
                        round(cast(iif(A.spr2 is null, 0, a.spr2) as float)/cast(SUM(B.one_year) as float) * 100,1) av_infl2spr2,
                        SUM(B.four_year) meta_fouryear, iif(A.dpt2_ref is null, 0, a.dpt2_ref) tot_dpt2_ref, iif(A.apo2_ref is null, 0, a.apo2_ref) tot_apo2_ref,
                        round(cast(iif(A.dpt2_ref is null, 0, a.dpt2_ref) as float)/cast(SUM(B.four_year) as float) * 100,1) av_dpt2_ref,
                        round(cast(iif(A.apo2_ref is null, 0, a.apo2_ref) as float)/cast(SUM(B.four_year) as float) * 100,1) av_apo2_ref,
                        SUM(B.girl9_13) meta_girl, iif(A.vph_girl is null, 0, a.vph_girl) tot_vph_girl, SUM(B.boy9_13) meta_boy,
                        iif(A.vph_boy is null, 0, a.vph_boy) tot_vph_boy,
                        round(cast(iif(A.vph_girl is null, 0, a.vph_girl) as float)/cast(SUM(B.girl9_13) as float) * 100,1) av_vph_girl,
                        round(cast(iif(A.vph_boy is null, 0, a.vph_boy) as float)/cast(SUM(B.boy9_13) as float) * 100,1) av_vph_boy,
                        SUM(B.pregnant) meta_girl, iif(A.dpta is null, 0, a.dpta) tot_dpta,
                        round(cast(iif(A.dpta is null, 0, a.dpta) as float)/cast(SUM(B.pregnant) as float) * 100,1) av_dpta,
                        SUM(B.adult60) meta_infl, iif(A.infl_adult is null, 0, a.infl_adult) tot_infl_adult, SUM(B.adult30) meta_neumo,
                        iif(A.neumo_adult is null, 0, a.neumo_adult) tot_neumo_adult,
                        round(cast(iif(A.infl_adult is null, 0, a.infl_adult) as float)/cast(SUM(B.adult60) as float) * 100,1) av_infl_adult,
                        round(cast(iif(A.neumo_adult is null, 0, a.neumo_adult) as float)/cast(SUM(B.adult30) as float) * 100,1) av_neumo_adult
                    FROM ESSALUD.dbo.boards_metacoverage AS B RIGHT JOIN ESSALUD.dbo.printCobertNominal A
                    ON A.cod_prov=B.cod_prov AND A.cod_dist=B.cod_dist where b.anio='2024'
                    GROUP BY B.provincia, B.distrito, A.bcg, A.hvb, a.rota2, a.apo3, a.penta3, a.infl2, a.neumo3, a.varicel, a.spr1, a.ama, a.hav, a.spr2,
                    dpt2_ref, apo2_ref, a.vph_girl, a.vph_boy, a.dpta, a.infl_adult, a.neumo_adult
                    DROP TABLE ESSALUD.dbo.printCobertNominal""")
        cont = 10
        num = 1
        # print(c.fetchall())
        data = []
        for a in c.fetchall():
            datos = {'provincia': a[0],
                     'distrito': a[1],
                     'meta_rn': a[2],
                     'bcg': 0 if a[3] == None else a[3],
                     'hvb': 0 if a[4] == None else a[4],
                     'av_bcg': a[5],
                     'av_hvb': a[6],
                     'meta_lessyear': a[7],
                     'rota2': 0 if a[8] == None else a[8],
                     'apo3': 0 if a[9] == None else a[9],
                     'penta3': 0 if a[10] == None else a[10],
                     'infl2': 0 if a[11] == None else a[11],
                     'av_rota2': a[12],
                     'av_apo3': a[13],
                     'av_penta3': a[14],
                     'av_infl2': a[15],
                     'meta_oneyear': a[16],
                     'neumo3': 0 if a[17] == None else a[17],
                     'varicel': 0 if a[18] == None else a[18],
                     'spr1': 0 if a[19] == None else a[19],
                     'ama': 0 if a[20] == None else a[20],
                     'hav': 0 if a[21] == None else a[21],
                     'spr2': 0 if a[22] == None else a[22],
                     'av_neumo3': a[23],
                     'av_varicel': a[24],
                     'av_spr1': a[25],
                     'av_ama': a[26],
                     'av_hav': a[27],
                     'av_spr2': a[28],
                     'meta_fouryear': a[29],
                     'dpt2': 0 if a[30] == None else a[30],
                     'apo2': 0 if a[31] == None else a[31],
                     'av_dpt2': a[32],
                     'av_apo2': a[33],
                     'meta_girl': a[34],
                     'girl': 0 if a[35] == None else a[35],
                     'meta_boy': a[36],
                     'boy': 0 if a[37] == None else a[37],
                     'av_girl': a[38],
                     'av_boy': a[39],
                     'meta_dpta': a[40],
                     'dpta': 0 if a[41] == None else a[41],
                     'av_dpta': a[42],
                     'meta_infl': a[43],
                     'infl_adult': 0 if a[44] == None else a[44],
                     'meta_neumo': a[45],
                     'neumo_adult': 0 if a[46] == None else a[46],
                     'av_infl': a[47],
                     'av_adul': a[48],
                    }

            data.append(datos)

        for nom in data:
            ws.cell(row=cont, column=1).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=1).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=1).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=1).value = num

            ws.cell(row=cont, column=2).alignment = Alignment(horizontal="left")
            ws.cell(row=cont, column=2).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=2).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=2).value = nom['provincia']

            ws.cell(row=cont, column=3).alignment = Alignment(horizontal="left")
            ws.cell(row=cont, column=3).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=3).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=3).value = nom['distrito']

            ws.cell(row=cont, column=4).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=4).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=4).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=4).value = nom['meta_rn']

            ws.cell(row=cont, column=5).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=5).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=5).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=5).value = nom['bcg']

            ws.cell(row=cont, column=6).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=6).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            traffic = '⬤'
            if nom['av_bcg'] < 41:
                ws.cell(row=cont, column=6).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_bcg'] > 40 and nom['av_bcg'] < 61:
                ws.cell(row=cont, column=6).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_bcg'] > 60 and nom['av_bcg'] < 95:
                ws.cell(row=cont, column=6).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_bcg'] > 94:
                ws.cell(row=cont, column=6).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=6).value = str(nom['av_bcg'])+' % '+traffic

            ws.cell(row=cont, column=7).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=7).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=7).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=7).value = nom['hvb']

            ws.cell(row=cont, column=8).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=8).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=8).font = Font(name='Calibri', size=9)
            if nom['av_hvb'] < 41:
                ws.cell(row=cont, column=8).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_hvb'] > 40 and nom['av_hvb'] < 61:
                ws.cell(row=cont, column=8).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_hvb'] > 60 and nom['av_hvb'] < 95:
                ws.cell(row=cont, column=8).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_hvb'] > 94:
                ws.cell(row=cont, column=8).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=8).value = str(nom['av_hvb'])+' % '+traffic

            ws.cell(row=cont, column=9).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=9).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=9).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=9).value = nom['meta_lessyear']

            ws.cell(row=cont, column=10).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=10).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=10).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=10).value = nom['rota2']

            ws.cell(row=cont, column=11).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=11).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=11).font = Font(name='Calibri', size=9)
            if nom['av_rota2'] < 41:
                ws.cell(row=cont, column=11).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_rota2'] > 40 and nom['av_rota2'] < 61:
                ws.cell(row=cont, column=11).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_rota2'] > 60 and nom['av_rota2'] < 95:
                ws.cell(row=cont, column=11).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_rota2'] > 94:
                ws.cell(row=cont, column=11).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=11).value = str(nom['av_rota2'])+' % '+traffic

            ws.cell(row=cont, column=12).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=12).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=12).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=12).value = nom['apo3']

            ws.cell(row=cont, column=13).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=13).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=13).font = Font(name='Calibri', size=9)
            if nom['av_apo3'] < 41:
                ws.cell(row=cont, column=13).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_apo3'] > 40 and nom['av_apo3'] < 61:
                ws.cell(row=cont, column=13).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_apo3'] > 60 and nom['av_apo3'] < 95:
                ws.cell(row=cont, column=13).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_apo3'] > 94:
                ws.cell(row=cont, column=13).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=13).value = str(nom['av_apo3'])+' % '+traffic

            ws.cell(row=cont, column=14).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=14).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=14).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=14).value = nom['penta3']

            ws.cell(row=cont, column=15).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=15).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=15).font = Font(name='Calibri', size=9)
            if nom['av_penta3'] < 41:
                ws.cell(row=cont, column=15).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_penta3'] > 40 and nom['av_penta3'] < 61:
                ws.cell(row=cont, column=15).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_penta3'] > 60 and nom['av_penta3'] < 95:
                ws.cell(row=cont, column=15).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_penta3'] > 94:
                ws.cell(row=cont, column=15).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=15).value = str(nom['av_penta3'])+' % '+traffic

            ws.cell(row=cont, column=16).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=16).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=16).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=16).value = nom['infl2']

            ws.cell(row=cont, column=17).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=17).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=17).font = Font(name='Calibri', size=9)
            if nom['av_infl2'] < 41:
                ws.cell(row=cont, column=17).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_infl2'] > 40 and nom['av_infl2'] < 61:
                ws.cell(row=cont, column=17).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_infl2'] > 60 and nom['av_infl2'] < 95:
                ws.cell(row=cont, column=17).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_infl2'] > 94:
                ws.cell(row=cont, column=17).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=17).value = str(nom['av_infl2'])+' % '+traffic

            ws.cell(row=cont, column=18).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=18).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=18).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=18).value = nom['meta_oneyear']

            ws.cell(row=cont, column=19).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=19).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=19).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=19).value = nom['neumo3']

            ws.cell(row=cont, column=20).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=20).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=20).font = Font(name='Calibri', size=9)
            if nom['av_neumo3'] < 41:
                ws.cell(row=cont, column=20).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_neumo3'] > 40 and nom['av_neumo3'] < 61:
                ws.cell(row=cont, column=20).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_neumo3'] > 60 and nom['av_neumo3'] < 95:
                ws.cell(row=cont, column=20).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_neumo3'] > 94:
                ws.cell(row=cont, column=20).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=20).value = str(nom['av_neumo3'])+' % '+traffic

            ws.cell(row=cont, column=21).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=21).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=21).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=21).value = nom['varicel']

            ws.cell(row=cont, column=22).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=22).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=22).font = Font(name='Calibri', size=9)
            if nom['av_varicel'] < 41:
                ws.cell(row=cont, column=22).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_varicel'] > 40 and nom['av_varicel'] < 61:
                ws.cell(row=cont, column=22).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_varicel'] > 60 and nom['av_varicel'] < 95:
                ws.cell(row=cont, column=22).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_varicel'] > 94:
                ws.cell(row=cont, column=22).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=22).value = str(nom['av_varicel'])+' % '+traffic

            ws.cell(row=cont, column=23).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=23).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=23).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=23).value = nom['spr1']

            ws.cell(row=cont, column=24).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=24).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=24).font = Font(name='Calibri', size=9)
            if nom['av_spr1'] < 41:
                ws.cell(row=cont, column=24).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_spr1'] > 40 and nom['av_spr1'] < 61:
                ws.cell(row=cont, column=24).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_spr1'] > 60 and nom['av_spr1'] < 95:
                ws.cell(row=cont, column=24).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_spr1'] > 94:
                ws.cell(row=cont, column=24).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=24).value = str(nom['av_spr1'])+' % '+traffic

            ws.cell(row=cont, column=25).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=25).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=25).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=25).value = nom['ama']

            ws.cell(row=cont, column=26).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=26).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=26).font = Font(name='Calibri', size=9)
            if nom['av_ama'] < 41:
                ws.cell(row=cont, column=26).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_ama'] > 40 and nom['av_ama'] < 61:
                ws.cell(row=cont, column=26).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_ama'] > 60 and nom['av_ama'] < 95:
                ws.cell(row=cont, column=26).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_ama'] > 94:
                ws.cell(row=cont, column=26).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=26).value = str(nom['av_ama'])+' % '+traffic

            ws.cell(row=cont, column=27).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=27).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=27).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=27).value = nom['hav']

            ws.cell(row=cont, column=28).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=28).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=28).font = Font(name='Calibri', size=9)
            if nom['av_hav'] < 41:
                ws.cell(row=cont, column=28).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_hav'] > 40 and nom['av_hav'] < 61:
                ws.cell(row=cont, column=28).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_hav'] > 60 and nom['av_hav'] < 95:
                ws.cell(row=cont, column=28).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_hav'] > 94:
                ws.cell(row=cont, column=28).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=28).value = str(nom['av_hav'])+' % '+traffic

            ws.cell(row=cont, column=29).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=29).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=29).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=29).value = nom['spr2']

            ws.cell(row=cont, column=30).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=30).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=30).font = Font(name='Calibri', size=9)
            if nom['av_spr2'] < 41:
                ws.cell(row=cont, column=30).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_spr2'] > 40 and nom['av_spr2'] < 61:
                ws.cell(row=cont, column=30).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_spr2'] > 60 and nom['av_spr2'] < 95:
                ws.cell(row=cont, column=30).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_spr2'] > 94:
                ws.cell(row=cont, column=30).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=30).value = str(nom['av_spr2'])+' % '+traffic

            ws.cell(row=cont, column=31).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=31).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=31).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=31).value = nom['meta_fouryear']

            ws.cell(row=cont, column=32).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=32).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=32).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=32).value = nom['dpt2']

            ws.cell(row=cont, column=33).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=33).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=33).font = Font(name='Calibri', size=9)
            if nom['av_dpt2'] < 41:
                ws.cell(row=cont, column=33).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_dpt2'] > 40 and nom['av_dpt2'] < 61:
                ws.cell(row=cont, column=33).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_dpt2'] > 60 and nom['av_dpt2'] < 95:
                ws.cell(row=cont, column=33).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_dpt2'] > 94:
                ws.cell(row=cont, column=33).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=33).value = str(nom['av_dpt2'])+' % '+traffic

            ws.cell(row=cont, column=34).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=34).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=34).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=34).value = nom['apo2']

            ws.cell(row=cont, column=35).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=35).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=35).font = Font(name='Calibri', size=9)
            if nom['av_apo2'] < 41:
                ws.cell(row=cont, column=35).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_apo2'] > 40 and nom['av_apo2'] < 61:
                ws.cell(row=cont, column=35).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_apo2'] > 60 and nom['av_apo2'] < 95:
                ws.cell(row=cont, column=35).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_apo2'] > 94:
                ws.cell(row=cont, column=35).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=35).value = str(nom['av_apo2'])+' % '+traffic

            ws.cell(row=cont, column=36).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=36).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=36).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=36).value = nom['meta_girl']

            ws.cell(row=cont, column=37).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=37).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=37).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=37).value = nom['girl']

            ws.cell(row=cont, column=38).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=38).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=38).font = Font(name='Calibri', size=9)
            if nom['av_girl'] < 41:
                ws.cell(row=cont, column=38).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_girl'] > 40 and nom['av_girl'] < 61:
                ws.cell(row=cont, column=38).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_girl'] > 60 and nom['av_girl'] < 95:
                ws.cell(row=cont, column=38).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_girl'] > 94:
                ws.cell(row=cont, column=38).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=38).value = str(nom['av_girl'])+' % '+traffic

            ws.cell(row=cont, column=39).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=39).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=39).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=39).value = nom['meta_boy']

            ws.cell(row=cont, column=40).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=40).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=40).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=40).value = nom['boy']

            ws.cell(row=cont, column=41).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=41).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=41).font = Font(name='Calibri', size=9)
            if nom['av_boy'] < 41:
                ws.cell(row=cont, column=41).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_boy'] > 40 and nom['av_boy'] < 61:
                ws.cell(row=cont, column=41).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_boy'] > 60 and nom['av_boy'] < 95:
                ws.cell(row=cont, column=41).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_boy'] > 94:
                ws.cell(row=cont, column=41).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=41).value = str(nom['av_boy'])+' % '+traffic

            ws.cell(row=cont, column=42).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=42).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=42).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=42).value = nom['meta_dpta']

            ws.cell(row=cont, column=43).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=43).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=43).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=43).value = nom['dpta']

            ws.cell(row=cont, column=44).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=44).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=44).font = Font(name='Calibri', size=9)
            if nom['av_dpta'] < 41:
                ws.cell(row=cont, column=44).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_dpta'] > 40 and nom['av_dpta'] < 61:
                ws.cell(row=cont, column=44).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_dpta'] > 60 and nom['av_dpta'] < 95:
                ws.cell(row=cont, column=44).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_dpta'] > 94:
                ws.cell(row=cont, column=44).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=44).value = str(nom['av_dpta'])+' % '+traffic

            ws.cell(row=cont, column=45).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=45).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=45).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=45).value = nom['meta_infl']

            ws.cell(row=cont, column=46).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=46).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=46).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=46).value = nom['infl_adult']

            ws.cell(row=cont, column=47).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=47).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=47).font = Font(name='Calibri', size=9)
            if nom['av_infl'] < 41:
                ws.cell(row=cont, column=47).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_infl'] > 40 and nom['av_infl'] < 61:
                ws.cell(row=cont, column=47).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_infl'] > 60 and nom['av_infl'] < 95:
                ws.cell(row=cont, column=47).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_infl'] > 94:
                ws.cell(row=cont, column=47).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=47).value = str(nom['av_infl'])+' % '+traffic

            ws.cell(row=cont, column=48).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=48).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=48).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=48).value = nom['meta_neumo']

            ws.cell(row=cont, column=49).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=49).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=49).font = Font(name='Calibri', size=9)
            ws.cell(row=cont, column=49).value = nom['neumo_adult']

            ws.cell(row=cont, column=50).alignment = Alignment(horizontal="center")
            ws.cell(row=cont, column=50).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
            ws.cell(row=cont, column=50).font = Font(name='Calibri', size=9)
            if nom['av_adul'] < 41:
                ws.cell(row=cont, column=50).font = Font(name='Calibri', size=10, color='FF2929')
            elif nom['av_adul'] > 40 and nom['av_adul'] < 61:
                ws.cell(row=cont, column=50).font = Font(name='Calibri', size=10, color='FF9900')
            elif nom['av_adul'] > 60 and nom['av_adul'] < 95:
                ws.cell(row=cont, column=50).font = Font(name='Calibri', size=10, color='00B050')
            elif nom['av_adul'] > 94:
                ws.cell(row=cont, column=50).font = Font(name='Calibri', size=10, color='4472C4')

            ws.cell(row=cont, column=50).value = str(nom['av_adul'])+' % '+traffic

            cont = cont+1
            num = num+1

        nombre_archivo = "DEIT_PASCO COBERTURA DE VACUNACION 2024.xlsx"
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        ws.title = 'NOMINAL NIÑOS RN'
        wb.save(response)
        return response

