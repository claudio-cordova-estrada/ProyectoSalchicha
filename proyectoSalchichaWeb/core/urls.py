from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('carrito', carrito, name="carrito"),
    path('compra', compra, name="compra"),
    path('login', login, name="login"),
    path('registrarse', registrarse, name="registrarse"),
]
