"""
URL configuration for mi_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import (
    ProyectoListView, 
    ProyectoCreateView, 
    ProyectoDetailView, 
    TareaCreateView,
    ProyectoUpdateView,
    ProyectoDeleteView,
    TareaToggleView,
    TareaDeleteView,
    SignUpView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro',SignUpView.as_view(),name='registro'),
    path('', ProyectoListView.as_view(), name='lista_proyectos'),
    path('nuevo-proyecto/', ProyectoCreateView.as_view(), name='crear_proyecto'),
    path('proyecto/<int:pk>/', ProyectoDetailView.as_view(), name='detalle_proyecto'),
    path('proyecto/<int:pk>/editar/', ProyectoUpdateView.as_view(), name='editar_proyecto'), # Nuevo
    path('proyecto/<int:pk>/eliminar/', ProyectoDeleteView.as_view(), name='eliminar_proyecto'), # Nuevo
    path('proyecto/<int:proyecto_id>/nueva-tarea/', TareaCreateView.as_view(), name='crear_tarea'),
    path('proyecto/<int:pk>/toggle/', TareaToggleView.as_view(), name='toggle_tarea'),
    path('tarea/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='eliminar_tarea'),
]
