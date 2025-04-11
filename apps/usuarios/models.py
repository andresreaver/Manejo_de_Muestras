from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    ROLES_CHOICES = [
        ('Admin', 'Administrador'),
        ('Gestor', 'Gestor'),
        ('Operacion', 'Operacion'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfilusuario')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=20)
    rol = models.CharField(max_length=20, choices=ROLES_CHOICES)

    def es_admin(self):
        return self.rol == 'Admin'

    def es_gestor(self):
        return self.rol == 'Gestor'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

