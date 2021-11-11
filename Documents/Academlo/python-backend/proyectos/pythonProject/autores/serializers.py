from rest_framework.serializers import ModelSerializer

from autores.models import Autor

# get (list) and not admin
class AutorSerializer(ModelSerializer):
    #autores = AutorSerializer(many=True)

    class Meta:
        model = Autor
        fields = '__all__' #['nombre', 'id']


# post
class CrearAutorSerializer(ModelSerializer):


    class Meta:
        model = Autor
        fields = '__all__' #['nombre', 'id']


# Retrieve and Admin
class DetalleAutorSerializer(ModelSerializer):


    class Meta:
        model = Autor
        fields = '__all__'

