from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from libros.models import Libro
from libros.paginations import CustomPagination
from libros.serializers import CrearLibroSerializer, DetalleLibroSerializer, LibroSerializer


@api_view(http_method_names=['GET', 'POST'])

def libros(request):
    if request.method == 'POST':
        serialized = CrearLibroSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data=serialized.data
        )


    if request.method == 'GET':
        libros = Libro.objects.all()
        serialized = CrearLibroSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

class LibroViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CustomPagination

    #def create(self, request, *args, **kwargs):

