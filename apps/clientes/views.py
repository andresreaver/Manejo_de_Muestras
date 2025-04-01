from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'clientes/crear_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})
