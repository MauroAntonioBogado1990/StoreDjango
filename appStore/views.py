from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#posteriormente para poder ver las vistas, tenemos que crear el archivo urls.py
def inicio(request):
    return render(request, 'paginas/inicio.html')

def articulos(request):
    return render(request, 'paginas/articulos.html')


#agregamos las vistas
def verarticulos(request):
    return render(request, 'articulos/index.html')

def crear(request):
    return render(request, 'articulos/crear.html')

def editar(request):
    return render(request, 'articulos/editar.html')

def borrar(request):
    return render(request, )



    