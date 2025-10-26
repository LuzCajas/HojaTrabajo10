from django import forms
from .models import Estudiante, Administrador, Publicacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'escritor', 'autorizado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'escritor': forms.Select(attrs={'class': 'form-control'}),
            'autorizado': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')