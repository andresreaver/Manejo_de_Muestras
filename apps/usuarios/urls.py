from django.urls import path

from apps.usuarios import services
from apps.usuarios.views import lista_usuarios, crear_usuario, editar_usuario, eliminar_usuario

urlpatterns = [
    path('login/', services.user_login, name="user_login"),
    path('logout/', services.user_logout, name="user_logout"),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:id>/', editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
]