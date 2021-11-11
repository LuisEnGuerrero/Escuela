from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from autores.models import Autor
from autores.serializers import AutorSerializer
from libros.models import Libro

"""
def mi_vista(request):
    #if request == 'GET':

        autores = Autor.objects.all()
        contexto = {
            'autores': autores
        }
        return render(request, 'autores/lista.html', contexto)

def autor_id(request, id):
    print(id)
    autor = Autor.objects.all(id=id)
    contexto = {
        'autor': autor
    }
    return render(request, 'autores/detalle.html', contexto)

class AutoresView(View):
    http_method_names = ['post', 'get']

    def get(self, request):
        autores = Autor.objects.all()
        contexto = {
            'autores': autores
        }
        return render(request, 'autores/lista.http', contexto)

    def post(self, request):
        Autor.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            direccion=request.POST['direccion'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
        )
        return self.get(request)



class AutorDetailView(View):
    http_method_names = ['post', 'get', 'push', 'delete']

    def get(self, request, id):
        autor = Autor.objects.all(id=id)
        contexto = {
            'autor': autor
        }
        return render(request, 'autores/detalle.html', contexto)

    def post(self, request, id):
        pass

    def push(self, request, id):
        pass

    def delete(self, request, id):
        pass
"""

class AutoresViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


@action(methods=['GET', 'POST'], detail=True)
def autores(self, request, pk=None):
    libro = Libro.objects.all()

    if request.method == 'GET':
        autores = libro.autores.all()
        serialized = AutorSerializer(autores, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )
    if request.method == 'POST':
        print(request.data)
        return Response(status=status.HTTP_200_OK)

@action(methods=['POST'], detail=True)
def publicar(self, request, pk=None):
    libro = self.get_object()
    libro.publicado = True
    libro.save()

    return Response(status=status.HTTP_200_OK)

@action(methods=['GET'], detail=False)
def order(self, request):
    order_by = '-id'
    if 'order_by' in self.request.query_params:
        order_by = self.request.query_params['order_by']
    queryset = self.get_queryset().order_by(order_by)
    serializer_class = self.get_serializer_class()
    serialized = serializer_class(queryset, many=True)
    return Response(
        status=status.HTTP_200_OK,
        data=serialized.data
    )

@action(methods=['POST'], detail=False)
def reset(self, request):
    queryset = self.get_queryset()
    for i in queryset:
        i.publicado = False
        i.save()
    return Response(status=status.HTTP_200_OK)

@action(methods=['POST'], detail=False)
def autorLess(self, request):
    queryset = self.get_queryset()
    for i in queryset:
        del(i.autores)
    return Response(status=status.HTTP_200_OK)