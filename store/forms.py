from django import forms
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import Register

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=PasswordInput)
    class Meta:
        model = Register
        fields = ('fullname', 'email','password')
        labels = {
            'fullname':'Nome Completo',
            'password':'Senha',
        }