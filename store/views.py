from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from .models import Register

# Create your views here.

def store(request):
    return render(request, 'store.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return  HttpResponse('Hello World!')

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/register.html', {'form':form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('store')
    