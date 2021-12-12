from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart")
]