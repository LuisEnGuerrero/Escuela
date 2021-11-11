from rest_framework.serializers import ModelSerializer

from libros.models import Libro

# get (list) and not admin
class LibroSerializer(ModelSerializer):
    #autores = AutorSerializer(many=True)

    class Meta:
        model = Libro
        fields = '__all__' #['nombre', 'id']


# post
class CrearLibroSerializer(ModelSerializer):


    class Meta:
        model = Libro
        fields = '__all__' #['nombre', 'id']


# Retrieve and Admin
class DetalleLibroSerializer(ModelSerializer):


    class Meta:
        model = Libro
        fields = '__all__'

