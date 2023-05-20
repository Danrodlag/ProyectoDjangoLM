from django import forms
from .models import Vehiculos


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['fabricante', 'modelo', 'npasajeros', 'peso', 'caballos', 'color', 'cencubicos', 'idcomercial']
