
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comerciales, Vehiculos
from .forms import VehiculoForm, ComForm


# Create your views here.


def index(request):
    num_coches = Vehiculos.objects.all().count()
    return render(request, 'index.html', context={'num_coches': num_coches})


def verTodos(request):
    lista_coches = Vehiculos.objects.all()
    return render(request, 'Vertodos.html', context={'lista_coches': lista_coches})


def nuevo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de lista de coches
    else:
        form = VehiculoForm()

    return render(request, 'Insnueva.html', {'form': form})


def verCoche(request, id):
    coche = get_object_or_404(Vehiculos, id=id)
    return render(request, 'Inscreada.html', {'coche': coche})


def actualizar(request, id):
    coche = get_object_or_404(Vehiculos, id=id)

    if request.method == 'POST':

        form = VehiculoForm(request.POST, instance=coche)
        if form.is_valid():

            form.save()
            return redirect('index')  # Redirigir al detalle del coche modificado
    else:
        form = VehiculoForm(instance=coche)

    return render(request, 'Actualiza.html', {'form': form, 'coche': coche})


def eliminar(request, id):
    coche = get_object_or_404(Vehiculos, id=id)

    if request.method == 'POST':
        coche.delete()
        return redirect('verTodos')  # Redirigir a la lista de coches o a donde desees

    return render(request, 'Elimina.html', {'coche': coche})


def nue_com(request):
    if request.method == 'POST':
        form = ComForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de lista de coches
    else:
        form = ComForm()

    return render(request, 'insCom.html', {'form': form})


def mod_com(request, id):
    comercial = get_object_or_404(Comerciales, id=id)

    if request.method == 'POST':

        form = ComForm(request.POST, instance=comercial)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ComForm(instance=comercial)

    return render(request, 'modCom.html', {'form': form, 'comercial': comercial})


def ver_comerciales(request):
    lista_comerciales = Comerciales.objects.all()
    # cant = Vehiculos.objects.annotate(num_coch=Count('idcomercial'))
    return render(request, 'ver_comerciales.html', context={'lista_comerciales': lista_comerciales})


def ver_comercial(request, id):

    com = get_object_or_404(Comerciales, id=id)
    return render(request, 'comercial.html', {'com': com})


def eliminar_com(request, id):
    com = get_object_or_404(Comerciales, id=id)

    if request.method == 'POST':
        com.delete()
        return redirect('ver_comerciales')

    return render(request, 'elim_com.html', {'com': com})