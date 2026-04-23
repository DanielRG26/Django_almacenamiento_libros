from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')


# TODO: Módulo de Libros a continuación (Espacio para Jesús)
from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'fecha_publicacion', 'autor', 'isbn')
    list_filter = ('autor', 'genero', 'fecha_publicacion')
