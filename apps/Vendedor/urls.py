from django.urls import path
from .views import  (
    VendedorListView,
    VendedorCreateView,
    VendedorUpdateView,
    VendedorDeleteView,
)

app_name = 'Vendedor'

urlpatterns = [
    path('', VendedorListView.as_view(), name='Vendedor_list'),
    path('create/', VendedorCreateView.as_view(), name='Vendedor_create'),
    path('update/<int:pk>/', VendedorUpdateView.as_view(), name='Vendedor_update'),
    path('delete/<int:pk>/', VendedorDeleteView.as_view(), name='Vendedor_delete'),
]