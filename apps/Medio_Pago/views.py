from django.views.generic import ListView, CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Medio_Pago

class Medio_PagoListView(ListView):
   model = Medio_Pago
   template_name = 'Medio_Pagos/list.html'
   context_object_name = 'Medio_Pagos' 

class Medio_PagoCreateView(CreateView):
   model = Medio_Pago
   fields = '__all__'
   template_name = 'Medio_Pagos/create.html'
   success_url = reverse_lazy('Medio_Pagos:Medio_Pago_list')


class Medio_PagoUpdateView(UpdateView):
   model = Medio_Pago
   fields = '__all__'
   template_name = 'Medio_Pagos/update.html'
   success_url = reverse_lazy('Medio_Pagos:Medio_Pago_list')

class Medio_PagoDeleteView(DeleteView):
   model = Medio_Pago
   template_name = 'Medio_Pagos/delete.html'
   success_url = reverse_lazy('Medio_Pagos:Medio_Pago_list')