from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import SolicitarMuestraForm, SeguimientoMuestraForm, LegalizarMuestraForm
from .models import Registro

def solicitar_muestra(request):
    if request.method == 'POST':
        form = SolicitarMuestraForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.estado = "SOLICITADA"
            registro.save()
            return redirect('seguimiento_muestra')
    else:
        form = SolicitarMuestraForm()

    return render(request, 'muestras_balalaika/solicitar_muestra.html',{'form': form})

def seguimiento_muestra(request):
    #Obtener muestras en estado Solicitada y en proceso
    muestras = Registro.objects.filter(estado__in=["SOLICITADA", "EN PROCESO"])

    return render(request, 'muestras_balalaika/seguimiento_muestra.html', {'muestras':muestras})

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

    return render(request,'muestras_balalaika/actualizar_muestra.html',{'form':form, 'registro':registro})

def marcar_sin_existencia(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    registro.estado = "SIN EXISTENCIA"
    registro.save()
    return redirect('seguimiento_muestra')

def lista_registros(request):
    registros = Registro.objects.all()
    return render(request,'muestras_balalaika/lista_registros.html',{'registros':registros})





            

def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == "POST":
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm(instance=registro)

    return render(request, 'muestras_balalaika/editar_registro.html', {'form': form, 'registro': registro})

def eliminar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == "POST":
        registro.delete()
        return redirect('lista_registros')

    return render(request, 'muestras_balalaika/eliminar_registro.html', {'registro': registro})

def buscar_registro(request):
    query = request.GET.get('q', '').strip()
    resultados = None

    if query:
        resultados = Registro.objects.filter(
            Q(cliente__icontains=query) |
            Q(comercial__icontains=query) |
            Q(referencia__icontains=query)
        )
    return render(request, 'muestras_balalaika/buscar_registro.html', {'resultados': resultados, 'query': query})

def entregar_muestra(request):
    #Filtrar las muestras que tengan estado en proceso
    muestras_en_proceso = Registro.objects.filter(estado="EN PROCESO")

    return render(request, 'muestras_balalaika/entrega_muestra.html', {'muestras_en_proceso':muestras_en_proceso})

def actualizar_entrega(request, pk):
    registro = get_object_or_404(Registro, pk=pk)

    if request.method == 'POST':
        form = LegalizarMuestraForm (request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.estado = "ENTREGADO"
            registro.save()
            return redirect('entrega_muestra')

    else:
        form = SeguimientoMuestraForm(instance=registro)

    return render(request,'muestras_balalaika/actualizar_entrega.html', {'form':form, 'registro':registro})
            