from django.views.generic import ListView, CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Usuario

class UsuarioListView(ListView):
   model = Usuario
   template_name = 'Usuarios/list.html'
   context_object_name = 'Usuarios' 

class UsuarioCreateView(CreateView):
   model = Usuario
   fields = '__all__'
   template_name = 'Usuarios/create.html'
   success_url = reverse_lazy('Usuarios:Usuario_list')


class UsuarioUpdateView(UpdateView):
   model = Usuario
   fields = '__all__'
   template_name = 'Usuarios/update.html'
   success_url = reverse_lazy('Usuarios:Usuario_list')

class UsuarioDeleteView(DeleteView):
   model = Usuario
   template_name = 'Usuarios/delete.html'
   success_url = reverse_lazy('Usuarios:Usuario_list')
