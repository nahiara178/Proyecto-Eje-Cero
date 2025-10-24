from django.views.generic import ListView, CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Venta_Compra

class Venta_CompraListView(ListView):
   model = Venta_Compra
   template_name = 'Venta_Compras/list.html'
   context_object_name = 'Venta_Compras' 

class Venta_CompraCreateView(CreateView):
   model = Venta_Compra
   fields = '__all__'
   template_name = 'Venta_Compras/create.html'
   success_url = reverse_lazy('Venta_Compras:Venta_Compra_list')


class Venta_CompraUpdateView(UpdateView):
   model = Venta_Compra
   fields = '__all__'
   template_name = 'Venta_Compras/update.html'
   success_url = reverse_lazy('Venta_Compras:Venta_Compra_list')

class Venta_CompraDeleteView(DeleteView):
   model = Venta_Compra
   template_name = 'Venta_Compras/delete.html'
   success_url = reverse_lazy('Venta_Compras:Venta_Compra_list')