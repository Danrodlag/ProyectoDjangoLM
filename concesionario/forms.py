from django import forms
from .models import Vehiculos, Comerciales


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['fabricante', 'modelo', 'npasajeros', 'peso', 'caballos', 'color', 'cencubicos', 'idcomercial']


class ComForm(forms.ModelForm):
    class Meta:
        model = Comerciales
        fields = ['nombre', 'apellido1', 'apellido2', 'fecha_incorporacion', 'comision']
