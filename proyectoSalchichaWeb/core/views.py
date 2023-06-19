from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def compra(request):
    return render(request, 'core/compra.html')

def login(request):
    return render(request, 'core/login.html')

def registrarse(request):
    return render(request, 'core/registrarse.html')
