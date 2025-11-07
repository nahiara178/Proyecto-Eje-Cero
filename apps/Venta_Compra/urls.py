from django.urls import path
from .views import  (
    Venta_CompraListView,
    Venta_CompraCreateView,
    Venta_CompraUpdateView,
    Venta_CompraDeleteView,
)

app_name = 'Venta_Compra'

urlpatterns = [
    path('', Venta_CompraListView.as_view(), name='Venta_Compra_list'),
    path('create/', Venta_CompraCreateView.as_view(), name='Venta_Compra_create'),
    path('update/<int:pk>/', Venta_CompraUpdateView.as_view(), name='Venta_Compra_update'),
    path('delete/<int:pk>/', Venta_CompraDeleteView.as_view(), name='Venta_Compra_delete'),
]