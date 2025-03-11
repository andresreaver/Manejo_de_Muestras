from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    ADMINISTRADOR = 'Administrador'
    GESTOR = 'Gestor'
    OPERACION = 'Operacion'

    ROLES_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (GESTOR, 'Gestor'),
        (OPERACION, 'Operacion'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=100)
    rol = models.CharField(max_length=15, choices=ROLES_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rol}"

