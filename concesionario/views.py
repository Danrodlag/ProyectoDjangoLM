from django.shortcuts import render
from .models import Comerciales, Vehiculos
# Create your views here.


def index(request):
    num_coches = Vehiculos.objects.all().count()
    return render(request, 'index.html', context={'num_coches': num_coches})


def verTodos(request):
    return None


def nuevo(request):
    return None


def verCoche(request):
    return None


def actualizar(request):
    return None


def eliminar(request):
    return None