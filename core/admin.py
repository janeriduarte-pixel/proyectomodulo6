from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'usuario')
    list_filter = ('usuario',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('-id',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'proyecto', 'completada')
    list_filter = ('completada', 'proyecto')
    search_fields = ('titulo',)
    list_editable = ('completada',)
    ordering =('-id',)
