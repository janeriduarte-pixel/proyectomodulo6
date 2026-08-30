from django.shortcuts import get_object_or_404, redirect 
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm, RegistroForm

# 1. LISTA DE PROYECTOS (Solo del usuario autenticado)
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'core/lista_proyectos.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

# 2. CREAR PROYECTO
class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/crear_proyecto.html'
    success_url = reverse_lazy('lista_proyectos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# 3. VER DETALLE DE UN PROYECTO
class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'core/detalle_proyecto.html'
    context_object_name = 'proyecto'

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

# 4. EDITAR PROYECTO
class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/crear_proyecto.html'
    success_url = reverse_lazy('lista_proyectos')

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

# 5. ELIMINAR PROYECTO
class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'core/eliminar_proyecto.html'
    success_url = reverse_lazy('lista_proyectos')

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

# 6. CREAR TAREA DENTRO DE UN PROYECTO
class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'core/crear_tarea.html'

    def form_valid(self, form):
        proyecto_id = self.kwargs['proyecto_id']
        proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=self.request.user)
        form.instance.proyecto = proyecto
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detalle_proyecto', kwargs={'pk': self.kwargs['proyecto_id']})


# 7. ALTERNAR ESTADO DE TAREA (Pendiente <-> Completada)
class TareaToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, id=pk, proyecto__usuario=request.user)
        tarea.completada = not tarea.completada
        tarea.save()
        return redirect('detalle_proyecto', pk=tarea.proyecto.id)

# 8. ELIMINAR TAREA DIRECTO (Sin HTML extra)
class TareaDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, id=pk, proyecto__usuario=request.user)
        proyecto_id = tarea.proyecto.id
        tarea.delete()
        return redirect('detalle_proyecto', pk=proyecto_id)

# 9. REGISTRO DE NUEVOS USUARIOS
class SignUpView(CreateView):
    form_class = RegistroForm  
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')
