from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
from ..muestras.models import COMERCIAL_CHOICES
from django.core.paginator import Paginator
from django.contrib import messages


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'clientes/form_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nombre')

    #Captura de info - Filtros
    estado = request.GET.get('estado', '')
    comercial = request.GET.get('comercial', '')
    ciudad = request.GET.get('ciudad', '')
    nombre = request.GET.get('nombre', '')
    departamento = request.GET.get('departamento', '')
    nit = request.GET.get('nit', '')
    pais = request.GET.get('pais', '')

    if estado:
        clientes = clientes.filter(estado__iexact=estado)
    if nombre:
        clientes = clientes.filter(nombre__icontains=nombre)
    if nit:
        clientes = clientes.filter(nit=nit)
    if comercial:
        clientes = clientes.filter(comercial=comercial)
    if ciudad:
        clientes = clientes.filter(ciudad=ciudad)
    if departamento:
        clientes = clientes.filter(departamento__icontains=departamento)
    if pais:
        clientes = clientes.filter(pais=pais)

    # Paginación
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    departamentos = Cliente.objects.values_list('departamento', flat=True).distinct().order_by('departamento')
    ciudades = Cliente.objects.values_list('ciudad', flat=True).distinct().order_by('ciudad')
    paises = Cliente.objects.values_list('pais', flat=True).distinct().order_by('pais')

    context = {
        'page_obj': page_obj,
        'clientes': clientes,
        'estado': estado,
        'comercial': comercial,
        'pais': pais,
        'ciudad': ciudad,
        'departamento': departamento,
        'departamentos': departamentos,
        'comercial_choices': COMERCIAL_CHOICES,
        'ciudades': ciudades,
        'paises': paises,

    }
    return render(request, 'clientes/lista_clientes.html', context)

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return  render(request, 'clientes/form_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, f'{cliente.nombre} fue eliminado exitosamente.')
        return redirect('lista_clientes')

    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})

