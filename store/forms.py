from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import UserRegisterModel
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username', 
            'email',
            'password1',
            'password2',
            )

        labels = {
            'username':'Usuario',
            'password1':'Senha',
            'password2':'Confirme a Senha'
        }

        def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user