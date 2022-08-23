from ast import Delete
from dataclasses import field
from distutils.command import upload
from statistics import mode
from django.db import models

# Create your models here.
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    precio = models.IntegerField()
    #imagen = models.ImageField(upload_to = 'imagenes/', verbose_name="Imagen", null=False, blank=True)
    descripcion = models.TextField(max_length=500, verbose_name="Descripcion")                
                   
    def __str__(self) -> str:
        fila =  self.nombre + ' - ' + self.descripcion
        return fila
    #eliminacion del registro
    def delete(self, using=None, keep_parents=False):
        #self.imagen.storage.delete(self.imagen.name)   
        super().delete()