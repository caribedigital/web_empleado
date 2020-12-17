from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):#esta función str devolverá en el template titulo y subtitulo con queryset
        return self.titulo + ' ' + self.subtitulo
