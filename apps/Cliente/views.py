from django.views.generic import ListView, CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Cliente

class ClienteListView(ListView):
   model = Cliente
   template_name = 'Clientes/list.html'
   context_object_name = 'Clientes' 

class ClienteCreateView(CreateView):
   model = Cliente
   fields = '__all__'
   template_name = 'Clientes/create.html'
   success_url = reverse_lazy('Clientes:Cliente_list')


class CLienteUpdateView(UpdateView):
   model = Cliente
   fields = '__all__'
   template_name = 'Clientes/update.html'
   success_url = reverse_lazy('Clientes:Cliente_list')

class ClienteDeleteView(DeleteView):
   model = Cliente
   template_name = 'Clientes/delete.html'
   success_url = reverse_lazy('Clientes:Cliente_list')


