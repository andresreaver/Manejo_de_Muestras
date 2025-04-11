from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import CrearUsuarioForm
from .services import crear_usuario_con_perfil, asignar_permisos_por_rol
from .decorators import rol_requerido


@login_required
@rol_requerido('Admin', 'Gestor')
def lista_usuarios(request):
    usuarios = User.objects.all().select_related('perfilusuario')
    return render(request, "usuarios/lista_usuarios.html", {'usuarios': usuarios})


@login_required
@rol_requerido('Admin', 'Gestor')
def crear_usuario(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            usuario = crear_usuario_con_perfil(form.cleaned_data)
            asignar_permisos_por_rol(usuario, form.cleaned_data['rol'])
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('lista_usuarios')
    else:
        form = CrearUsuarioForm()
    return render(request, "usuarios/crear_usuario.html", {'form': form})


@login_required
@rol_requerido('Admin')
def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    perfil = usuario.perfilusuario

    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario.username = datos['username']
            usuario.email = datos['email']
            usuario.first_name = datos['nombre']
            usuario.last_name = datos['apellido']
            if datos['password']:
                usuario.set_password(datos['password'])
            usuario.save()

            perfil.nombre = datos['nombre']
            perfil.apellido = datos['apellido']
            perfil.cedula = datos['cedula']
            perfil.cargo = datos['cargo']
            perfil.email = datos['email']
            perfil.celular = datos['celular']
            perfil.rol = datos['rol']
            perfil.save()

            asignar_permisos_por_rol(usuario, datos['rol'])
            messages.success(request, 'Usuario actualizado correctamente')
            return redirect('lista_usuarios')
    else:
        form = CrearUsuarioForm(initial={
            'username': usuario.username,
            'email': usuario.email,
            'nombre': perfil.nombre,
            'apellido': perfil.apellido,
            'cedula': perfil.cedula,
            'cargo': perfil.cargo,
            'celular': perfil.celular,
            'rol': perfil.rol,
        })

    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})


@login_required
@rol_requerido('Admin')
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})
