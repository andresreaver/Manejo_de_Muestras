from django import forms
from django.contrib.auth.models import User
from apps.usuarios.models import PerfilUsuario

class CrearUsuarioForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'})
    )
    apellido = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'})
    )
    cedula = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cédula'})
    )
    cargo = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el cargo'})
    )
    celular = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el celular'})
    )
    rol = forms.ChoiceField(
        choices=PerfilUsuario.ROLES_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el usuario"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingrese el correo electrónico"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["nombre"]
        user.last_name = self.cleaned_data["apellido"]
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            PerfilUsuario.objects.create(
                usuario=user,
                nombre=self.cleaned_data["nombre"],
                apellido=self.cleaned_data["apellido"],
                cedula=self.cleaned_data["cedula"],
                cargo=self.cleaned_data["cargo"],
                email=self.cleaned_data["email"],
                celular=self.cleaned_data["celular"],
                rol=self.cleaned_data["rol"],
            )
        return user
