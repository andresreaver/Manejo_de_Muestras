from django.urls import path
from .views import crear_cliente, lista_clientes

urlpatterns = [
    path('crear/', crear_cliente, name='crear_cliente'),
    path('lista/', lista_clientes, name='lista_clientes'),
]