from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from datetime import timedelta

from django.shortcuts import redirect, render, get_object_or_404

from .forms import SolicitarMuestraForm, SeguimientoMuestraForm, LegalizarMuestraForm
from .models import Registro, COMERCIAL_CHOICES, ESTADO_CHOICES
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils.timezone import now

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('lista_registros')
    return redirect('user_login')

def solicitar_muestra(request):
    if request.method == 'POST':
        form = SolicitarMuestraForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.estado = "SOLICITADA"
            registro.save()
            return redirect(reverse('seguimiento_muestra'))
    else:
        form = SolicitarMuestraForm()

    return render(request, 'muestras/solicitar_muestra.html',{'form': form})

def seguimiento_muestra(request):
    muestras = Registro.objects.filter(estado__in=["SOLICITADA"])
    return render(request, 'muestras/seguimiento_muestra.html', {'muestras':muestras})

def actualizar_muestra(request, pk):
    registro = get_object_or_404(Registro, pk=pk)

    if request.method == 'POST':
        form = SeguimientoMuestraForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.estado = "EN PROCESO"
            registro.save()
            return redirect('seguimiento_muestra') #redirige a la vista de seguimiento
    else:
        form = SeguimientoMuestraForm(instance=registro)

    return render(request,'muestras/actualizar_muestra.html',{'form':form, 'registro':registro})

def marcar_sin_existencia(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    registro.estado = "SIN EXISTENCIA"
    registro.save()
    return redirect('seguimiento_muestra')

def lista_registros(request):
    query = request.GET.get('q', '').strip()
    comercial = request.GET.get('comercial', '')
    estado = request.GET.get('estado','')
    referencia = request.GET.get('referencia', '')
    cliente = request.GET.get('cliente', '')

    #Hay filtros activos
    hay_filtro = any([query, comercial, estado, referencia, cliente])

    #Muestra por defecto los registros del ultimo mes
    registros = Registro.objects.all()
    if not hay_filtro:
        ultimo_mes = now() - timedelta(days=30)
        registros = registros.filter(fecha_solicitud__gte=ultimo_mes)

    #Aplicar busqueda general
    if query:
        registros = registros.filter(
            Q(cliente__icontains=query)|
            Q(comercial__icontains=query)|
            Q(referencia__icontains=query)
        )

    #Aplicar filtros adicionales si se seleccionan
    if comercial:
        registros = registros.filter(comercial=comercial)
    if estado:
        registros = registros.filter(estado=estado)
    if referencia:
        registros = registros.filter(referencia__icontains=referencia)
    if cliente:
        registros = registros.filter(cliente__icontains=cliente)

    # Asegurar un ordenamiento estable antes de la paginación
    registros = registros.order_by('-fecha_solicitud', 'id')

    #Paginacion
    paginator = Paginator(registros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'muestras/lista_registros.html',{
        'page_obj':page_obj,
        'query':query,
        'comercial_choices':COMERCIAL_CHOICES,
        'estado_choices':ESTADO_CHOICES,
        'comercial_selected':comercial,
        'estado_selected':estado,
        'referencia':referencia,
        'cliente':cliente,
    })

@login_required
@permission_required('muestras.delete_registro', raise_exception=True)
def eliminar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == "POST":
        registro.delete()
        return redirect('lista_registros')

    return render(request, 'muestras/eliminar_registro.html', {'registro': registro})

@login_required
@permission_required('muestras.change_registro', raise_exception=True)
def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == "POST":
        form = SolicitarMuestraForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = SolicitarMuestraForm(instance=registro)

    return render(request, 'muestras/editar_registro.html', {'form': form, 'registro': registro})

def entregar_muestra(request):
    #Filtrar las muestras que tengan estado en proceso
    muestras_en_proceso = Registro.objects.filter(estado="EN PROCESO").order_by('-fecha_solicitud')
    return render(request, 'muestras/entrega_muestra.html', {'muestras_en_proceso':muestras_en_proceso})

def actualizar_entrega(request, pk):
    registro = get_object_or_404(Registro, pk=pk)

    if request.method == 'POST':
        form = LegalizarMuestraForm (request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.estado = "ENTREGADO"
            registro.save()
            return redirect(reverse('entrega_muestra'))

    else:
        form = LegalizarMuestraForm(instance=registro)

    return render(request,'muestras/actualizar_entrega.html', {'form':form, 'registro':registro})

