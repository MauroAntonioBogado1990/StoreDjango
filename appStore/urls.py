from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('articulos', views.articulos, name='articulos'),
    path('verarticulos',views.verarticulos,name='verarticulos'),
    path('articulos/crear', views.crear, name = 'crear'),
    path('articulos/editar', views.editar, name = 'editar'),
]

