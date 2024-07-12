from django.views.generic import TemplateView, View
from django.http.request import QueryDict, MultiValueDict
from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.models import Group
from .models import Person, User

from .forms import PersonForm
import json
import time
from django.db.models import Count

# Create your views here.
class PersonView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PersonForm
        context['eid'] =1
        return context


class CreatePerson(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                person_data = form.save(commit=False)
                person_data.user_create = request.user.username
                person_data.save()

                data = User()
                data.username = request.POST['pdoc']
                data.set_password(request.POST['pdoc'])
                data.id_person = Person.objects.get(pdoc=request.POST['pdoc'])
                data.save()

                Dataperson = Person.objects.filter(pk=person_data.id)
                data = serializers.serialize('json', Dataperson, indent=2, use_natural_foreign_keys=True)
                return HttpResponse(data, content_type='application/json')

            else:
                return HttpResponse({'success': 'Error in aplication'}, content_type='application/json')

    def put(self, request, *args, **kwargs):
            if request.content_type.startswith('multipart'):
                request.PUT, files = request.parse_file_upload(request.META, request)
            else:
                request.PUT = QueryDict(request.body)

            if request.method == 'PUT':
                obj_format = Person.objects.get(pk=request.PUT['pk'])
                form = PersonForm(data=request.PUT or None, instance=obj_format)
                if form.is_valid():
                    data_update = form.save(commit=False)
                    data_update.user_update = request.user.username
                    data_update.date_update = time.strftime("%Y-%m-%d")
                    data_update.save()
                    data_saved = Person.objects.filter(pk=data_update.pk)
                    format_data = serializers.serialize('json', data_saved, indent=2, use_natural_foreign_keys=True)
                    return HttpResponse(format_data, content_type='application/json')
                else:
                    return HttpResponse({'success': 'Error in aplication'}, content_type='application/json')


class searchPerson(View):
    def get(self, request, *args, **kwargs):
        DataPerson= Person.objects.filter(pdoc = request.GET['dni'])
        DataPerson = serializers.serialize('json', DataPerson, indent=2, use_natural_foreign_keys=True)
        DataPerson = json.loads(DataPerson)

        if DataPerson:
            DataUser= User.objects.filter(id_person_id= DataPerson[0]['pk'])
            DataUser = serializers.serialize('json', DataUser, indent=2, use_natural_foreign_keys=True)
            DataUser = json.loads(DataUser)
        else:
            DataUser=[]

        return HttpResponse(json.dumps(DataPerson + DataUser), content_type='application/json')


class CrudUser(View):
    def put(self, request, *args, **kwargs):
        if request.content_type.startswith('multipart'):
            request.PUT, files = request.parse_file_upload(request.META, request)
        else:
            request.PUT = QueryDict(request.body)

        if request.method == 'PUT':
            user = User.objects.get(pk=request.PUT['pid'])
            user.set_password(request.PUT['password'])
            user.save()
            return HttpResponse(status=200, content_type='application/json')
