from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']


# TODO: Módulo de Libros a continuación (Espacio para Jesús)
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }
