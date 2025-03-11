from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import PerfilUsuario

def crear_usuario_con_perfil(datos):
    usuario = User.objects.create(
        username=datos["username"],
        email=datos["email"],
        first_name=datos["nombre"],
        last_name=datos["apellido"],
    )
    usuario.set_password(datos["password"])
    usuario.save()


    PerfilUsuario.objects.create(
        usuario=usuario,
        nombre=datos["nombre"],
        apellido=datos["apellido"],
        cedula=datos["cedula"],
        cargo=datos["cargo"],
        email=datos["email"],
        celular=datos["celular"],
        rol=datos["rol"]
    )
    return usuario

def user_login(request):
    if request.user.is_authenticated:
        return redirect('lista_registros')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.first_name}")
            return redirect('lista_registros')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'usuarios/login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('user_login')