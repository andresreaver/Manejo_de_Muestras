from django.db import models

from apps.muestras.models import COMERCIAL_CHOICES

ESTADO_CLIENTE = [
    ("Nuevo", "Nuevo"),
    ("Codificado", "Codificado"),
]

class Cliente(models.Model):
    estado = models.CharField(max_length=15, choices=ESTADO_CLIENTE, default="Seleccionar", null=False)
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120, unique=True)
    nombre_contacto = models.CharField(max_length=120, blank=True, null=True)
    direccion = models.CharField(max_length=120, blank=True, null=True)
    ciudad = models.CharField(max_length=120, blank=True, null=True)
    departamento = models.CharField(max_length=120, blank=True, null=True)
    pais = models.CharField(max_length=120, blank=True, null=True)
    telefono = models.CharField(max_length=120, blank=True, null=True)
    celular = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    comercial = models.CharField(max_length=20, choices=COMERCIAL_CHOICES)

    fecha_primera_muestra = models.DateField(null=True, blank=True)
    fecha_ultima_muestra = models.DateField(null=True, blank=True)
    hizo_compra = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
