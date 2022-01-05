from django import forms
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import UserRegisterModel
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = UserRegisterModel
        fields = (
            'username', 
            'email',
            'password',
            'confirm_password',
            )

        widgets = {
            'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput()
        }

        labels = {
            'username':'Usuario',
            'password':'Senha',
            'confirm_password':'Confirme a Senha'
        }

        def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user