from django.db import models

# Create your models here.
from autores.models import Autor
from editoriales.models import Editorial


class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    caratula = models.BinaryField()
    paginas = models.IntegerField()
    publicado = models.BooleanField()
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.SET_NULL,
        null=True,
        related_name='libros'
    )
    autores = models.ManyToManyField(Autor, related_name='libros')
    #editores = models.ManyToManyField(Autor, through='EditoresLibro')

    def str(self):
        return f'{self.nombre} | Editorial: {self.editorial}'

"""
class EditoresLibro(models.Model):
    nombre = models.CharField(max_length=100)
    caratula = models.BinaryField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
"""