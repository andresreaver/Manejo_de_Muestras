from django.urls import path

from . import services
from .views import crear_usuario, lista_usuarios

urlpatterns = [
    path('login/', services.user_login, name="user_login"),
    path('logout/', services.user_logout, name="user_logout"),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
]