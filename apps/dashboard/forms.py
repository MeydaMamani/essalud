from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control has-feedback-left'
        self.fields['username'].widget.attrs['placeholder']='Usuario'
        self.fields['password'].widget.attrs['class']='form-control has-feedback-left'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

    def clean(self):
        user_found = User.objects.filter(username = self.cleaned_data['username']).exists()
        if not user_found:
            self.add_error('username', 'Usuario no Encontrado.')
        else:
            user = User.objects.get(username = self.cleaned_data['username'])
            if  not user.check_password(self.cleaned_data['password']):
                self.add_error('password', 'Contraseña Incorrecta.')


class ChangePassForm(forms.Form):
    new_pass = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña',
            'v-model':'form.new_pass',
        }
    ))
    new_pass_r = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control m-b-10 m-t-10',
            'placeholder': 'Repita contraseña',
            'v-model': 'form.new_pass_r',
        }
    ))
