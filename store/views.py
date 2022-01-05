from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm
from .models import UserRegisterModel

# Create your views here.

def store(request):
    return render(request, 'store.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return  HttpResponse('Teste!')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Vocẽ foi Registrado com Sucesso!')
            return redirect('store')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form':form})


def login_view(request):
    pass