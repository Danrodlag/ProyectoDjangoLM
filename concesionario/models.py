from django.db import models

# Create your models here. Aquí se crean las tablas.


class Comerciales(models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    fecha_incorporacion = models.DateField()
    comision = models.FloatField()

    class Meta:
        db_table = 'comerciales'
        ordering = ['fecha_incorporacion']


class Vehiculos(models.Model):
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    npasajeros = models.PositiveSmallIntegerField()
    peso = models.PositiveIntegerField()
    caballos = models.FloatField()
    color = models.CharField(max_length=100)
    cencubicos = models.PositiveIntegerField()
    idcomercial = models.ForeignKey(Comerciales, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vehiculos'
        ordering = ['caballos']


"""
    def get_absolute_url(self):
        Devuelve la url para localizar la instancia de un libro concreto
        return reverse('libro_detail', args=[str(self.id)])
    def __str__(self):
        Representación en forma cadena del objeto
        return self.isbn

"""