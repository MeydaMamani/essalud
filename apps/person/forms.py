from django import forms
from .models import Person, User

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets= {
            'eid': forms.TextInput(attrs={
                'class': 'form-control',
                'v-model': 'form.eid',
            }),
            'typedoc': forms.Select(attrs={
                'class': 'form-control custom-select',
                'v-model': 'form.typedoc'
            }),
            'pdoc': forms.TextInput(attrs={
                'class': 'form-control',
                'v-model': 'form.pdoc'
            }),
            'last_name0': forms.TextInput(attrs={
                'class': 'form-control',
                'v-model': 'form.last_name0'
            }),
            'last_name1': forms.TextInput(attrs={
                'class': 'form-control',
                'v-model': 'form.last_name1'
            }),
            'names': forms.TextInput(attrs={
                'class': 'form-control',
                'v-model': 'form.names'
            }),
            'birthday': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'v-model': 'form.birthday',
            }),
            'sex': forms.Select(attrs={
                'class': 'form-control custom-select',
                'v-model': 'form.sex'
            }),
            'pmail': forms.TextInput(attrs={
                'class': 'form-control ',
                'v-model': 'form.pmail'
            }),
            'phone': forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'v-model': 'form.phone'
            }),
            'institution': forms.TextInput(attrs={
                'class': 'form-control ',
                'v-model': 'form.institution'
            }),
        }
