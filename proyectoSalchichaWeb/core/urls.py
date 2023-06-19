from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="home"),
    path('carrito', carrito, name="home"),
    path('compra', compra, name="home"),
    path('login', login, name="home"),
    path('registrarse', registrarse, name="home"),
]
