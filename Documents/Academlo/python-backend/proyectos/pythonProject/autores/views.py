from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View

from autores.models import Autor

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
