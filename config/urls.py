from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from apps.core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.urls')),
    path('muestras/', include('apps.muestras.urls')),

    #Paginas de Login y Logout
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #Enviar al home si no autentica
    path('', lambda request: redirect('home') if request.user.is_authenticated else redirect('login')),

    #Pagina de bienvenida para usuarios
    path('home/', login_required(home), name='home'),
]
