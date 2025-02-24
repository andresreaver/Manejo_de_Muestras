from django import forms
from django.forms import Select
from .models import Registro, COMERCIAL_CHOICES, TIPO_CHOICES

class SolicitarMuestraForm(forms.ModelForm):
    METROS_SOLICITADOS_CHOICES = [(i, str(i)) for i in range (1,6)]

    comercial = forms.ChoiceField(choices=COMERCIAL_CHOICES, required=True)
    referencia = forms.CharField(max_length=15)
    color = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0', 'max': '9999'}),
        required=True
    )
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, required=True)
    hdr = forms.CharField(max_length=15, required=False)
    metros_solicitados = forms.ChoiceField(choices=METROS_SOLICITADOS_CHOICES, required=True)


    class Meta:
        model = Registro
        exclude = ['estado','fecha_solicitud']
        fields = [
            'cliente',
            'comercial',
            'referencia',
            'color',
            'tipo',
            'metros_solicitados',
            'hdr',
        ]
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'cliente': forms.TextInput(attrs={'style': 'text-transform: uppercase;'}),
            'tipo': Select(choices=TIPO_CHOICES),
            'metros_solicitados': Select(),
        }


class SeguimientoMuestraForm(forms.ModelForm):

    fecha_envio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    metros_enviados = forms.DecimalField(max_digits=5, decimal_places=1)
    kg_enviados = forms.DecimalField(max_digits=5, decimal_places=1, required=False)
    hdr = forms.CharField(max_length=15, required=False)
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, required=True)

    class Meta:
        model = Registro
        exclude = ['estado']
        fields = ['fecha_envio','metros_enviados','kg_enviados','hdr','tipo']

class LegalizarMuestraForm(forms.ModelForm):
    fecha_llegada = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    remision = forms.CharField(max_length=10)
    fecha_remision = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    doc_sag = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Registro
        fields = ['fecha_llegada','remision','fecha_remision', 'doc_sag']



"""class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'fecha_envio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_llegada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_remision': forms.DateInput(attrs={'type': 'date'}),
            'metros_solicitados': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'metros_enviados': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'kg_enviados': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'cliente': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del cliente'}),
            'comercial': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del comercial'}),
            'referencia': forms.TextInput(attrs={'placeholder': 'Referencia del producto'}),
            'color': forms.TextInput(attrs={'placeholder': 'Ejemplo: Rojo, Azul'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Tipo de material o categoría'}),
            'estado': forms.TextInput(attrs={'placeholder': 'Estado del pedido'}),
            'guia': forms.TextInput(attrs={'placeholder': 'Número de guía de envío'}),
            'remision': forms.TextInput(attrs={'placeholder': 'Número de remisión'}),
            'doc_sag': forms.TextInput(attrs={'placeholder': 'Documento SAG'}),
            'bodega': forms.TextInput(attrs={'placeholder': 'Ubicación en bodega'}),
        }"""