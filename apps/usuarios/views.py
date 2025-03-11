from .forms import CrearUsuarioForm
from .services import crear_usuario_con_perfil
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

def es_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(es_admin)
def lista_usuarios(request):
    usuarios = User.objects.all().select_related('perfilUsuario')
    return render(request, "usuarios/lista_usuarios.html", {'usuarios': usuarios})

@user_passes_test(es_admin)
def crear_usuario(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            crear_usuario_con_perfil(form.cleaned_data)
            return redirect('lista_usuarios')
        else:
            form.CrearUsuarioForm()

        return render(request,"usuarios/crear_usuario.html",{'form':form})
