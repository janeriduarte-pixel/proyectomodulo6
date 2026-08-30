from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proyecto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe tu proyecto aquí...'}),
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'completada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nueva tarea'}),
        }


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username'] # Las contraseñas se agregan automáticamente

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Este le agrega la clase 'form-control' de Bootstrap a cada cajita de texto, para ordenar el Form que Django genera en el apartado de registro manualmente.
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

