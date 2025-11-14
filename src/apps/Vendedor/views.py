from django.views.generic import ListView, CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Vendedor

class VendedorListView(ListView):
   model = Vendedor
   template_name = 'Vendedores/list.html'
   context_object_name = 'Vendedores' 

class VendedorCreateView(CreateView):
   model = Vendedor
   fields = '__all__'
   template_name = 'Vendedores/create.html'
   success_url = reverse_lazy('Vendedores:Vendedor_list')


class VendedorUpdateView(UpdateView):
   model = Vendedor
   fields = '__all__'
   template_name = 'Vendedores/update.html'
   success_url = reverse_lazy('Vendedores:Vendedor_list')

class VendedorDeleteView(DeleteView):
   model = Vendedor
   template_name = 'Vendedores/delete.html'
   success_url = reverse_lazy('Vendedores:Vendedor_list')