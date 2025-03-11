from django import forms
from django.contrib.auth.models import User
from apps.usuarios.models import PerfilUsuario



class CrearUsuarioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    cedula = forms.CharField(max_length=20)
    cargo = forms.CharField(max_length=20)
    celular = forms.CharField(max_length=20)
    rol = forms.ChoiceField(choices=PerfilUsuario.ROLES_CHOICES)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]