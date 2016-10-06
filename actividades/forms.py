from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from models import Actividades
from crispy_forms.helper import FormHelper

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'autofocus':'autofocus', 'placeholder':'Usuario'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder':'Clave'}))

class ActividadesForm(ModelForm):
    class Meta:
        model = Actividades
        fields = ['casos_de_uso', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(ActividadesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
