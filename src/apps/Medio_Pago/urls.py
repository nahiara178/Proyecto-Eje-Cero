from django.urls import path
from .views import  (
    Medio_PagoListView,
    Medio_PagoCreateView,
    Medio_PagoUpdateView,
    Medio_PagoDeleteView,
)

app_name = 'Medio_Pago'

urlpatterns = [
    path('', Medio_PagoListView.as_view(), name='Medio_Pago_list'),
    path('create/', Medio_PagoCreateView.as_view(), name='Medio_Pago_create'),
    path('update/<int:pk>/', Medio_PagoUpdateView.as_view(), name='Medio_Pago_update'),
    path('delete/<int:pk>/', Medio_PagoDeleteView.as_view(), name='Medio_Pago_delete'),
]