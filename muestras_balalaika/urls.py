from django.urls import path
from . import views, auth_views
from .views import eliminar_registro, \
    solicitar_muestra, seguimiento_muestra, actualizar_muestra, marcar_sin_existencia, entregar_muestra, \
    actualizar_entrega, lista_registros, editar_registro

urlpatterns = [
    path('login/', auth_views.user_login, name="user_login"),
    path('logout/', auth_views.user_logout, name="user_logout"),
    path('', views.home_redirect, name='home_redirect'),
    path('muestras/', views.lista_registros, name='lista_registros'),# Redirecciona /muestras/ a la lista de registros
    path('solicitar/', solicitar_muestra, name='solicitar_muestra'),
    path('lista/', lista_registros, name='lista_registros'),
    path('editar/<int:pk>/', editar_registro, name='editar_registro'),
    path('eliminar/<int:pk>/', eliminar_registro, name='eliminar_registro'),
    path('seguimiento/', seguimiento_muestra, name='seguimiento_muestra'),
    path('actualizar/<int:pk>/', actualizar_muestra, name='actualizar_muestra'),
    path('marcar_sin_existencia/<int:pk>/', marcar_sin_existencia, name='marcar_sin_existencia'),
    path('entrega/', entregar_muestra, name='entrega_muestra'),
    path('actualizar_entrega/<int:pk>/', actualizar_entrega, name='actualizar_entrega'),

]

