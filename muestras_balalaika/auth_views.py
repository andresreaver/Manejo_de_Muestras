from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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