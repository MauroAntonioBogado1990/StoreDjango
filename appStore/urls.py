from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('articulos', views.articulos, name='articulos'),
    path('verarticulos',views.verarticulos,name='verarticulos'),
    path('articulos/crear', views.crear, name = 'crear'),
    path('articulos/editar', views.editar, name = 'editar'),
    path('borrar/<int:id>', views.borrar, name = 'borrar'),
    path('articulos/editar/<int:id>', views.editar, name = 'editar'),
    path('buscar',views.buscar, name = 'buscar'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

