from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from .models import UserRegisterModel
from django.contrib.auth.forms import AuthenticationForm

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
        messages.error(request, 'Sem Sucesso no Registro. Informação Invalida!')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Seja bem vindo')
                return redirect('store')
            else:
                messages.error(request, 'Email ou Senha invalidos!')
        else:
            messages.error(request, 'Usuario ou Senha invalidos')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request, 'user/login.html', context)