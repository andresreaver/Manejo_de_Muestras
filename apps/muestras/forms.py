from django import forms
from django.forms import Select

from .models import Registro, COMERCIAL_CHOICES, TIPO_CHOICES

class SolicitarMuestraForm(forms.ModelForm):
    METROS_SOLICITADOS_CHOICES = [(i, str(i)) for i in range (1,6)]

    comercial = forms.ChoiceField(
        choices=COMERCIAL_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-select"}
    ))
    referencia = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Referencia completa"})
    )
    color = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", 'min': '0', 'max': '9999',"placeholder": "Ej. 0000"}),
        required=True
    )
    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    hdr = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Hoja de ruta"})
    )
    metros_solicitados = forms.ChoiceField(
        choices=METROS_SOLICITADOS_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-select"})
    )


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
            'cliente': forms.TextInput(attrs={"class": "form-control", "placeholder": "Cliente en mayúsculas"}),
            'referencia': forms.TextInput(attrs={"class": "form-control"}),
            'comercial': forms.Select(attrs={"class": "form-select"}),
            'tipo': forms.Select(attrs={"class": "form-select"}),
            'color': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. 0000"}),
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date', "class":"form-control"}),
            'metros_solicitados': forms.Select(attrs={"class": "form-select"}),
            'hdr': forms.TextInput(attrs={"class": "form-control", "placeholder": "Hoja de ruta"}),
        }


class SeguimientoMuestraForm(forms.ModelForm):

    fecha_envio = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    metros_enviados = forms.DecimalField(
        max_digits=5, decimal_places=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5.0', 'step': '0.1'}),
        required=True
    )
    kg_enviados = forms.DecimalField(
        max_digits=5, decimal_places=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Opcional', 'step': '0.1'}),
        required=False
    )
    hdr = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hoja de Ruta'}),
        required=False
    )
    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    class Meta:
        model = Registro
        exclude = ['estado']
        fields = ['fecha_envio','metros_enviados','kg_enviados','hdr','tipo']

class LegalizarMuestraForm(forms.ModelForm):
    fecha_llegada = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    remision = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Remisión'}),
        required=True
    )
    fecha_remision = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    doc_sag = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento SAG'}),
        required=True
    )

    class Meta:
        model = Registro
        fields = ['fecha_llegada', 'remision', 'fecha_remision', 'doc_sag']