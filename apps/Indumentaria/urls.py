from django.urls import path
from .views import  (
   IndumentariaListView,
   IndumentariaCreateView,
   IndumentariaUpdateView,
   IndumentariaDeleteView,
)

app_name = 'Indumentaria'

urlpatterns = [
    path('',IndumentariaListView.as_view(), name='Indumentaria_list'),
    path('create/',IndumentariaCreateView.as_view(), name='Indumentaria_create'),
    path('update/<int:pk>/',IndumentariaUpdateView.as_view(), name='Indumentaria_update'),
    path('delete/<int:pk>/',IndumentariaDeleteView.as_view(), name='Indumentaria_delete'),
]