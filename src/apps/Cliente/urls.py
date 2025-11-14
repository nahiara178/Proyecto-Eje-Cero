from django.urls import path
from .views import  (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)

app_name = 'Cliente'

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]