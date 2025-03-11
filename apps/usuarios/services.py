from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import PerfilUsuario

def crear_usuario_con_perfil(datos):
    usuario = User.objects.create_user(
        username=datos["username"],
        email=datos["email"],
        password=datos["password"]
    )
    PerfilUsuario.objects.create(
        usuario=usuario,
        nombre=datos["nombre"],
        apellidos=datos["apellidos"],
        cedula=datos["cedula"],
        cargo=datos["cargo"],
        celular=datos["celular"],
        rol=datos["rol"]
    )
    return usuario

def user_login(request):
    if request.user.is_authenticated:
        return redirect('lista_registros')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_registros')
        else:
            return render(request, 'muestras_balalaika/login.html', {'error':'Usuario o Contraseña Incorrectos'})

    return render(request, 'muestras_balalaika/login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('user_login')

