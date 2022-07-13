from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from .models import Articulo
from .forms import ArticuloForm
# Create your views here.
#posteriormente para poder ver las vistas, tenemos que crear el archivo urls.py
def inicio(request):
    return render(request, 'paginas/inicio.html')

def articulos(request):
    return render(request, 'paginas/articulos.html')


#agregamos las vistas
def verarticulos(request):
    #agregado de form para la búsqueda de elementos
    articulos = Articulo.objects.all()
    
    return render(request, 'articulos/index.html', {'articulos' : articulos})


def buscar(request):
    #agregado de form para la búsqueda de elementos
    busqueda = request.GET.get("buscar")
    articulos = Articulo.objects.all()

    if busqueda:
        articulos = Articulo.objects.filter(
            Q(id__contains = busqueda) |
            Q(nombre__icontains = busqueda) |
            Q(precio__icontains = busqueda) |
            Q(descripcion__icontains = busqueda) 

        ).distinct()
    
    return render(request, 'articulos/buscar.html', {'articulos' : articulos})

#recibimos los archivos y además los enviamos para mostrar
def crear(request):
    formulario = ArticuloForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('articulos')
    return render(request, 'articulos/crear.html', {'formulario' : formulario})

def editar(request, id):
    articulos = Articulo.objects.get(id=id)
    formulario = ArticuloForm(request.POST or None,  request.FILES or None, instance = articulos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('articulos')
    return render(request, 'articulos/editar.html', {'formulario' : formulario})

def borrar(request, id):
    articulos = Articulo.objects.get(id=id)
    articulos.delete()
    return redirect('articulos' )



    