from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm
from .models import Register

# Create your views here.

def store(request):
    return render(request, 'store.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return  HttpResponse('Hello World!')
