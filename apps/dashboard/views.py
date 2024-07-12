from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, View

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect

from apps.person.models import Person
User = get_user_model()

from .forms import LoginForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard:home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    #verifica la petición
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        try:
            ObjPerson = Person.objects.get(pk=user.id_person.id)
            ObjUser = User.objects.get(pk=user.pk)
            self.request.session['sytem'] = {'eid': ObjPerson.eid_id, 'full_name': ObjPerson.last_name0+' '+ObjPerson.last_name1+', '+ObjPerson.names.title(),
                                            'doc': ObjPerson.pdoc, 'red': ObjUser.id_red.pk, 'redCode': ObjUser.id_red.code, 'redLevel': ObjUser.id_red.level,
                                            'redName': ObjUser.id_red.name,
                                            'redState': ObjUser.id_red.state
                                        }

        except:
            print("Hay un error en los valores de entrada")

        return super(LoginView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form3'] = ChangePassForm
    #     return context

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
