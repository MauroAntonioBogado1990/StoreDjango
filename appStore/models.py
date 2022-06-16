from dataclasses import field
from distutils.command import upload
from statistics import mode
from django.db import models

# Create your models here.
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to = 'imagenes/', verbose_name="Imagen", null=True)
    descripcion = models.TextField(max_length=500, verbose_name="Descripcion")                
                   