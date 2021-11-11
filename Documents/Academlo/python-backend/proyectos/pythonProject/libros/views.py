from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response

from libros.models import Libro


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
