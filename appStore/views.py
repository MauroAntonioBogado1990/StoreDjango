from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#posteriormente para poder ver las vistas, tenemos que crear el archivo urls.py
def inicio(request):
    return render(request, 'paginas/inicio.html')

def articulos(request):
    return render(request, 'paginas/articulos.html')

def verarticulos(request):
    return render(request, 'articulos/index.html')



    