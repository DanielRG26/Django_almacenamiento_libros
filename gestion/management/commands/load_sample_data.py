from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from gestion.models import Autor, Libro


class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos'

    def handle(self, *args, **options):
        # Verificar si ya existen datos
        if Autor.objects.exists():
            self.stdout.write(self.style.WARNING('Los datos de prueba ya existen. Saltando...'))
            return

        # Crear autores
        autores_data = [
            {
                'nombre': 'Gabriel García Márquez',
                'correo': 'gabriel@example.com',
                'nacionalidad': 'Colombiana',
                'fecha_nacimiento': date(1927, 3, 6),
                'biografia': 'Escritor y periodista colombiano, ganador del Premio Nobel de Literatura en 1982.'
            },
            {
                'nombre': 'Jorge Luis Borges',
                'correo': 'jorge@example.com',
                'nacionalidad': 'Argentina',
                'fecha_nacimiento': date(1899, 8, 24),
                'biografia': 'Escritor argentino, poeta, ensayista y traductor, considerado uno de los autores más influyentes del siglo XX.'
            },
            {
                'nombre': 'Isabel Allende',
                'correo': 'isabel@example.com',
                'nacionalidad': 'Chilena',
                'fecha_nacimiento': date(1942, 8, 2),
                'biografia': 'Escritora chilena, una de las autoras vivas más leídas en español en el mundo.'
            },
            {
                'nombre': 'Paulo Coelho',
                'correo': 'paulo@example.com',
                'nacionalidad': 'Brasileña',
                'fecha_nacimiento': date(1947, 8, 24),
                'biografia': 'Escritor y poeta brasileño, autor de "El Alquimista".'
            },
        ]

        autores = []
        for autor_data in autores_data:
            autor, created = Autor.objects.get_or_create(**autor_data)
            autores.append(autor)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Creado autor: {autor.nombre}'))

        # Crear libros
        libros_data = [
            {
                'titulo': 'Cien años de soledad',
                'fecha_publicacion': date(1967, 5, 30),
                'genero': 'Novela',
                'isbn': '978-0-06-088328-7',
                'autor': autores[0]  # García Márquez
            },
            {
                'titulo': 'El coronel no tiene quien le escriba',
                'fecha_publicacion': date(1961, 1, 1),
                'genero': 'Novela corta',
                'isbn': '978-84-206-0051-0',
                'autor': autores[0]  # García Márquez
            },
            {
                'titulo': 'Ficciones',
                'fecha_publicacion': date(1944, 8, 1),
                'genero': 'Cuentos',
                'isbn': '978-0-14-118257-9',
                'autor': autores[1]  # Borges
            },
            {
                'titulo': 'El Aleph',
                'fecha_publicacion': date(1949, 1, 1),
                'genero': 'Cuentos',
                'isbn': '978-84-206-0050-3',
                'autor': autores[1]  # Borges
            },
            {
                'titulo': 'La casa de los espíritus',
                'fecha_publicacion': date(1982, 10, 1),
                'genero': 'Novela',
                'isbn': '978-84-322-0840-7',
                'autor': autores[2]  # Isabel Allende
            },
            {
                'titulo': 'De amor y de sombra',
                'fecha_publicacion': date(1984, 1, 1),
                'genero': 'Novela',
                'isbn': '978-84-322-0841-4',
                'autor': autores[2]  # Isabel Allende
            },
            {
                'titulo': 'El Alquimista',
                'fecha_publicacion': date(1988, 1, 1),
                'genero': 'Novela filosófica',
                'isbn': '978-84-322-0842-1',
                'autor': autores[3]  # Paulo Coelho
            },
            {
                'titulo': 'Zahir',
                'fecha_publicacion': date(2005, 1, 1),
                'genero': 'Novela',
                'isbn': '978-84-322-0843-8',
                'autor': autores[3]  # Paulo Coelho
            },
        ]

        for libro_data in libros_data:
            libro, created = Libro.objects.get_or_create(**libro_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Creado libro: {libro.titulo}'))

        self.stdout.write(self.style.SUCCESS('\n✅ ¡Datos de prueba cargados correctamente!'))
