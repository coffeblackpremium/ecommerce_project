from django import forms
from django.forms import fields
from .models import Register

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Register
        fields = ('fullname', 'email','password')