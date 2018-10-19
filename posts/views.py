from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_lista(request):
    return render(request, "index.html")

def posts_crear(request):
    return HttpResponse("<h1>Hola a crear</h1>")

def posts_detalles(request):
    return HttpResponse("<h1>Hola a detalles</h1>")

def posts_actualizar(request):
    return HttpResponse("<h1>Hola a actualizar</h1>")

def posts_eliminar(request):
    return HttpResponse("<h1>Hola a eliminar</h1>")