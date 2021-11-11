import calendar

from django.db import models


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(calendar.Calendar)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.nombre} {self.apellido}'
