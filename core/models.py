from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos')
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
