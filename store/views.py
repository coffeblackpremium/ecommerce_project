from django.shortcuts import render

# Create your views here.

def store(request):
    return render(request, 'partials/base.html')

def cart(request):
    return render(request, 'cart.html')