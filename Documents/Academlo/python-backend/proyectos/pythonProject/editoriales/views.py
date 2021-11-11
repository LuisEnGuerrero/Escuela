from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer

"""
class EditorialesGenericView(ListView):
    model = Editorial
    context_object_name = 'editoriales'


class EditorialesNuevoView(CreateView):
    model = Editorial
    fields = ('nombre', 'direccion', 'cantidad_publicaciones')
    success_url = '/editoriales/'


class EditorialDetailView(DetailView):
    queryset = Editorial.objects.all()
    context_object_name = 'editorial'


class EditorialDetailViewApi(APIView):
    queryset = Editorial.objects.all()
    context_object_name = 'editorial'


class EditorialGenericView(ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class EditorialDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

"""

class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
