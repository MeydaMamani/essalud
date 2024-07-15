from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.core import serializers
from django.http import JsonResponse, HttpResponse, QueryDict
from datetime import datetime
import json

from django.db.models import Sum, F, FloatField, Case, When
from django.db.models.functions import Cast
from django.db import connection
from datetime import date, datetime

from apps.packages.models import PackChildFollow
from apps.main.models import Provincia, Distrito, Establecimiento
from apps.follow_up.models import Anemia

import datetime
import json
import locale

# library excel
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side, Color


class KidsView(TemplateView):
    template_name = 'kids/index.html'


class SearchKidsView(View):
    def get(self, request, *args, **kwargs):
        data_saved = PackChildFollow.objects.filter(documento=request.GET['doc'])
        format_data = serializers.serialize('json', data_saved, indent=2, use_natural_foreign_keys=True)
        return HttpResponse(format_data, content_type='application/json')


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


class NominalAnemia(View):
    def post(self, request, *args, **kwargs):
        dataList = []
        result = Anemia.objects.filter(anio=request.POST['anio'], mes=request.POST['mes']).values('establecimiento').annotate(menor=Sum(Case(When(num=1, then=1), default=0)),
                oneyear=Sum(Case(When(num=1, then=1), default=0)), twoyear=Sum(Case(When(num=1, then=2), default=0)))

        if request.POST['tipo'] == 'TODOS':
            if request.POST['red'] == 'TODOS':
                totProv = Anemia.objects.filter(anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

            elif request.POST['red'] != 'TODOS' and request.POST['dist'] == 'TODOS':
                totProv = Anemia.objects.filter(cod_prov=request.POST['red'], anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(cod_prov=request.POST['red'], anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

            elif request.POST['dist'] != 'TODOS' and request.POST['eess'] == 'TODOS':
                totProv = Anemia.objects.filter(cod_dist=request.POST['dist'], anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(cod_dist=request.POST['dist'], anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

            elif request.POST['eess'] != 'TODOS':
                totProv = Anemia.objects.filter(cod_eess=request.POST['eess'], anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(cod_eess=request.POST['eess'], anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

        else:
            if request.POST['red'] == 'TODOS':
                totProv = Anemia.objects.filter(anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

            elif request.POST['red'] != 'TODOS' and request.POST['dist'] == 'TODOS':
                totProv = Anemia.objects.filter(cod_prov=request.POST['red'], anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(cod_prov=request.POST['red'], anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

            elif request.POST['dist'] != 'TODOS' and request.POST['eess'] == 'TODOS':
                totProv = Anemia.objects.filter(cod_dist=request.POST['dist'], anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(cod_dist=request.POST['dist'], anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

            elif request.POST['eess'] != 'TODOS':
                totProv = Anemia.objects.filter(cod_eess=request.POST['eess'], anio=request.POST['anio'], mes=request.POST['mes']).values('provincia').annotate(total=Sum('den'))
                totNominal = Anemia.objects.filter(cod_eess=request.POST['eess'], anio=request.POST['anio'], mes=request.POST['mes'])
                totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

        dataList.append(list(totProv))
        dataList.append(totNominal)
        dataList.append(list(result))

        return HttpResponse(json.dumps(dataList), content_type='application/json')


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

        set_border(self, ws, "A2:S2", "medium", "57267C")
        set_border(self, ws, "A4:S4", "medium", "366092")
        set_border(self, ws, "A6:S6", "medium", "D9D9D9")

        img = Image('static/img/logoPrint.png')
        ws.add_image(img, 'A2')

        ws.merge_cells('B2:S2')
        ws.row_dimensions[2].height = 23

        ws.column_dimensions['A'].width = 6
        ws.column_dimensions['B'].width = 14
        ws.column_dimensions['C'].width = 33
        ws.column_dimensions['D'].width = 33
        ws.column_dimensions['F'].width = 33

        ws['B2'].font = Font(name='Aptos Narrow', size=11, bold=True, color='57267C')
        ws['B2'].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        ws['B2'] = 'ESSALUD PASCO: SEGUIMIENTO DE NIÑOS Y NIÑAS CON DX ANEMIA - ' + str(nameMonth).upper() + ' ' + str(request.GET['anio'])

        ws.merge_cells('A4:S4')
        ws['A4'].font = Font(name='Aptos Narrow', size=9, bold=True, color='305496')
        ws['A4'] = 'CODIFICACION: HVB: 90744   -   BCG: 90585'

        ws.merge_cells('A6:S6')
        ws['A6'].font = Font(name='Aptos Narrow', size=9, bold=True, color='757171')
        ws['A6'] = 'Fuente: BD HisMinsa con Fecha: ' + date.today().strftime('%Y-%m-%d') + ' a las 08:30 horas'

        ws['A8'] = '#'
        ws['A8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['A8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['A8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['A8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['B8'] = 'Provincia'
        ws['B8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['B8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['B8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['B8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['C8'] = 'Distrito'
        ws['C8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['C8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['C8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['C8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['D8'] = 'Establecimiento'
        ws['D8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['D8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['D8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['D8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['E8'] = 'Documento'
        ws['E8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['E8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['E8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['E8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['F8'] = 'Apellidos y Nombres'
        ws['F8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['F8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['F8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['F8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['G8'] = 'Fecha Nacido'
        ws['G8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['G8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['G8'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
        ws['G8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['H8'] = 'Dosaje 1'
        ws['H8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['H8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['H8'].fill = PatternFill(start_color='C7ECF0', end_color='C7ECF0', fill_type='solid')
        ws['H8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['I8'] = 'Resultado 1'
        ws['I8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['I8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['I8'].fill = PatternFill(start_color='C7ECF0', end_color='C7ECF0', fill_type='solid')
        ws['I8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['J8'] = 'Dosaje 2'
        ws['J8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['J8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['J8'].fill = PatternFill(start_color='F0E6C7', end_color='F0E6C7', fill_type='solid')
        ws['J8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['K8'] = 'Resultado 2'
        ws['K8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['K8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['K8'].fill = PatternFill(start_color='F0E6C7', end_color='F0E6C7', fill_type='solid')
        ws['K8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['L8'] = 'Dx Anemia 1'
        ws['L8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['L8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['L8'].fill = PatternFill(start_color='F0C7E6', end_color='F0C7E6', fill_type='solid')
        ws['L8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['M8'] = 'Dx Anemia 2'
        ws['M8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['M8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['M8'].fill = PatternFill(start_color='F0C7E6', end_color='F0C7E6', fill_type='solid')
        ws['M8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['N8'] = 'Nutrición 6'
        ws['N8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['N8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['N8'].fill = PatternFill(start_color='C7DBF0', end_color='C7DBF0', fill_type='solid')
        ws['N8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['O8'] = 'Nutrición 7'
        ws['O8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['O8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['O8'].fill = PatternFill(start_color='C7DBF0', end_color='C7DBF0', fill_type='solid')
        ws['O8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['P8'] = 'Nutrición 8'
        ws['P8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['P8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['P8'].fill = PatternFill(start_color='C7DBF0', end_color='C7DBF0', fill_type='solid')
        ws['P8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['Q8'] = 'Nutrición 9'
        ws['Q8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['Q8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['Q8'].fill = PatternFill(start_color='C7DBF0', end_color='C7DBF0', fill_type='solid')
        ws['Q8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['R8'] = 'Nutrición 10'
        ws['R8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['R8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['R8'].fill = PatternFill(start_color='C7DBF0', end_color='C7DBF0', fill_type='solid')
        ws['R8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        ws['S8'] = 'Nutrición 11'
        ws['S8'].font = Font(name='Aptos Narrow', size=10, bold=True)
        ws['S8'].alignment = Alignment(horizontal="center", vertical="center")
        ws['S8'].fill = PatternFill(start_color='C7DBF0', end_color='C7DBF0', fill_type='solid')
        ws['S8'].border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))

        if request.GET['tipo'] == 'TODOS':
            if request.GET['red'] == 'TODOS':
                totNominal = Anemia.objects.filter(anio=request.GET['anio'], mes=request.GET['mes'])

            elif request.GET['red'] != 'TODOS' and request.GET['dist'] == 'TODOS':
                totNominal = Anemia.objects.filter(cod_prov=request.GET['red'], anio=request.GET['anio'], mes=request.GET['mes'])

            elif request.GET['dist'] != 'TODOS' and request.GET['eess'] == 'TODOS':
                totNominal = Anemia.objects.filter(cod_dist=request.GET['dist'], anio=request.GET['anio'], mes=request.GET['mes'])

            elif request.GET['eess'] != 'TODOS':
                totNominal = Anemia.objects.filter(cod_eess=request.GET['eess'], anio=request.GET['anio'], mes=request.GET['mes'])

        else:
            if request.GET['red'] == 'TODOS':
                totNominal = Anemia.objects.filter(anio=request.GET['anio'], mes=request.GET['mes'])

            elif request.GET['red'] != 'TODOS' and request.GET['dist'] == 'TODOS':
                totNominal = Anemia.objects.filter(cod_prov=request.GET['red'], anio=request.GET['anio'], mes=request.GET['mes'])

            elif request.GET['dist'] != 'TODOS' and request.GET['eess'] == 'TODOS':
                totNominal = Anemia.objects.filter(cod_dist=request.GET['dist'], anio=request.GET['anio'], mes=request.GET['mes'])

            elif request.GET['eess'] != 'TODOS':
                totNominal = Anemia.objects.filter(cod_eess=request.GET['eess'], anio=request.GET['anio'], mes=request.GET['mes'])

        totNominal = json.loads(serializers.serialize('json', totNominal, indent=2, use_natural_foreign_keys=True))

        cont = 9
        cant = len(totNominal)
        num = 1
        if cant > 0:
            for nom in totNominal:
                ws.cell(row=cont, column=1).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=1).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=1).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=1).value = num

                ws.cell(row=cont, column=2).alignment = Alignment(horizontal="left")
                ws.cell(row=cont, column=2).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=2).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=2).value = nom['fields']['provincia']

                ws.cell(row=cont, column=3).alignment = Alignment(horizontal="left")
                ws.cell(row=cont, column=3).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=3).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=3).value = nom['fields']['distrito']

                ws.cell(row=cont, column=4).alignment = Alignment(horizontal="left")
                ws.cell(row=cont, column=4).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=4).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=4).value = nom['fields']['establecimiento']

                ws.cell(row=cont, column=5).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=5).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=5).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=5).value = nom['fields']['documento']

                ws.cell(row=cont, column=6).alignment = Alignment(horizontal="left")
                ws.cell(row=cont, column=6).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=6).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=6).value = nom['fields']['ape_nombres']

                ws.cell(row=cont, column=7).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=7).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=7).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=7).value = nom['fields']['fec_nac']

                ws.cell(row=cont, column=8).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=8).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=8).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=8).value = nom['fields']['dosaje1']

                ws.cell(row=cont, column=9).alignment = Alignment(horizontal="left")
                ws.cell(row=cont, column=9).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=9).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=9).value = nom['fields']['result1']

                ws.cell(row=cont, column=10).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=10).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=10).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=10).value = nom['fields']['dosaje2']

                ws.cell(row=cont, column=11).alignment = Alignment(horizontal="left")
                ws.cell(row=cont, column=11).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=11).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=11).value = nom['fields']['result2']

                ws.cell(row=cont, column=12).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=12).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=12).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=12).value = nom['fields']['dx_anemia1']

                ws.cell(row=cont, column=13).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=13).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=13).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=13).value = nom['fields']['dx_anemia2']

                ws.cell(row=cont, column=14).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=14).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=14).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=14).value = nom['fields']['nutricion6']

                ws.cell(row=cont, column=15).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=15).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=15).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=15).value = nom['fields']['nutricion7']

                ws.cell(row=cont, column=16).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=16).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=16).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=16).value = nom['fields']['nutricion8']

                ws.cell(row=cont, column=17).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=17).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=17).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=17).value = nom['fields']['nutricion9']

                ws.cell(row=cont, column=18).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=18).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=18).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=18).value = nom['fields']['nutricion10']

                ws.cell(row=cont, column=19).alignment = Alignment(horizontal="center")
                ws.cell(row=cont, column=19).border = Border(left=Side(border_style="thin", color="808080"), right=Side(border_style="thin", color="808080"), top=Side(border_style="thin", color="808080"), bottom=Side(border_style="thin", color="808080"))
                ws.cell(row=cont, column=19).font = Font(name='Calibri', size=9)
                ws.cell(row=cont, column=19).value = nom['fields']['nutricion11']

                cont = cont+1
                num = num+1

        nombre_archivo = "DEIT_PASCO SEGUIMIENTO DE NIÑOS CON DX ANEMIA.xlsx"
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        ws.title = 'NOMINAL NIÑOS RN'
        wb.save(response)
        return response

