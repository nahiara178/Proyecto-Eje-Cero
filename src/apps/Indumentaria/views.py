from django.views.generic import ListView, CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Indumentaria

class IndumentariaListView(ListView):
   model = Indumentaria
   template_name = 'Indumentarias/list.html'
   context_object_name = 'Indumentarias' 

class IndumentariaCreateView(CreateView):
   model = Indumentaria
   fields = '__all__'
   template_name = 'Indumentarias/create.html'
   success_url = reverse_lazy('Indumentarias:Indumentaria_list')


class IndumentariaUpdateView(UpdateView):
   model = Indumentaria
   fields = '__all__'
   template_name = 'Indumentarias/update.html'
   success_url = reverse_lazy('Indumentarias:Indumentaria_list')

class IndumentariaDeleteView(DeleteView):
   model = Indumentaria
   template_name = 'Indumentarias/delete.html'
   success_url = reverse_lazy('Indumentarias:Indumentaria_list')