from django.db import models
import datetime


COMERCIAL_CHOICES = [
        ('TEXTILES BALALAIKA', 'TEXTILES BALALAIKA'),
        ('ALEXANDER AVILA', 'ALEXANDER AVILA'),
        ('ANDREA VARELA', 'ANDREA VARELA'),
        ('CARLOS GARCIA', 'CARLOS GARCIA'),
        ('CATALINA SERNA', 'CATALINA SERNA'),
        ('CONSTANZA VARGAS', 'CONSTANZA VARGAS'),
        ('FREDY OCAMPO', 'FREDY OCAMPO'),
        ('JOSEFINA CORREDOR', 'JOSEFINA CORREDOR'),
        ('LOUIS BARBOSA', 'LOUIS BARBOSA'),
        ('OTROS', 'OTROS'),
    ]
TIPO_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('I', 'I'),
        ('O','0'),
    ]
ESTADO_CHOICES = [
        ('SOLICITADA', 'SOLICITADA'),
        ('EN PROCESO', 'EN PROCESO'),
        ('ENTREGADO', 'ENTREGADO'),
        ('SIN EXISTENCIA', 'SIN EXISTENCIA'),
    ]

class Registro(models.Model):

    fecha_solicitud = models.DateField(default=datetime.date.today)
    cliente = models.CharField(max_length=255)
    comercial = models.CharField(max_length=50, choices=COMERCIAL_CHOICES)
    referencia = models.CharField(max_length=50)
    color = models.IntegerField()
    metros_solicitados = models.DecimalField(max_digits=7, decimal_places=2)
    metros_enviados = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    kg_enviados = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    hdr = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='SOLICITADA')
    fecha_envio = models.DateField(default=datetime.date.today, null=True, blank=True)
    fecha_llegada = models.DateField(default=datetime.date.today, null=True, blank=True)
    remision = models.CharField(max_length=50, null=True, blank=True)
    fecha_remision = models.DateField(null=True, blank=True)
    doc_sag = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.cliente} - {self.fecha_solicitud} - {self.estado}"