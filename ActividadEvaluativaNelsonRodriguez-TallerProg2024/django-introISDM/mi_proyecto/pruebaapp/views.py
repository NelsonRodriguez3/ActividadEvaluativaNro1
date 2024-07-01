from django.shortcuts import render
from .models import MiModelo
from django.http import HttpResponse

def consultar_modelo(request):
    objetos = MiModelo.objects.all()
    return render(request, 'templates_consultas.html'), {'objetos': objetos}

def index(request):
    return HttpResponse("¡Hola Mundo! Esta es la página de inicio.")
# Create your views here.
