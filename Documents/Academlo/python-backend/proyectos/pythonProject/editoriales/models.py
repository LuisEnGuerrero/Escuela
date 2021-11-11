from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    activa = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cantidad_publicaciones = models.IntegerField()
    direccion = models.CharField(max_length=500, default='')

    def str(self):
        return self.nombre