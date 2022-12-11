from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)


class Mascota(models.Model):
    animal = models.CharField(max_length=100)
    edad = models.IntegerField()

class Vehiculo(models.Model):
    Marca = models.CharField(max_length=100)
    dueño = models.CharField(max_length=100)

