from django.db import models
from django.forms.widgets import PasswordInput

# Create your models here.

class UserRegisterModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=320)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    