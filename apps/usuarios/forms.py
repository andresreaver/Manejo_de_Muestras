from django import forms
from django.contrib.auth.models import User
from apps.usuarios.models import PerfilUsuario

class CrearUsuarioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    cedula = forms.CharField(max_length=20)
    cargo = forms.CharField(max_length=20)
    celular = forms.CharField(max_length=20)
    rol = forms.ChoiceField(choices=PerfilUsuario.ROLES_CHOICES)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['Nombre']
        user.last_name = self.cleaned_data['Apellidos']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            PerfilUsuario.objects.create(
                usuario=user,
                nombre=self.cleaned_data['Nombre'],
                apellido=self.cleaned_data['Apellido'],
                cedula=self.cleaned_data['Cedula'],
                cargo=self.cleaned_data['Cargo'],
                email=self.cleaned_data['Email'],
                celuar=self.cleaned_data['Celular'],
                rol=self.cleaned_data['Rol'],
            )
            return user