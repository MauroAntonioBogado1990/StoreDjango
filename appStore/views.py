from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#posteriormente para poder ver las vistas, tenemos que crear el archivo urls.py
def inicio(request):
    return HttpResponse("<h1>Creando la primera vista</h1>")