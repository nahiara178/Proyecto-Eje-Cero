from django.urls import path
from .views import  (
    UsuarioListView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
)

app_name = 'Usuario'

urlpatterns = [
    path('', UsuarioListView.as_view(), name='Usuario_list'),
    path('create/', UsuarioCreateView.as_view(), name='Usuario_create'),
    path('update/<int:pk>/', UsuarioUpdateView.as_view(), name='Usuario_update'),
    path('delete/<int:pk>/', UsuarioDeleteView.as_view(), name='Usuario_delete'),
]