from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('cart/checkout/', views.checkout, name="checkout"),
    path('register/', views.register, name="user_register")
]