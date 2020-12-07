from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', null=True)#cambiado de nullBooleanField por BooleanField y por arg (null=True) en django 4.0

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['-name']
        unique_together = ('name', 'short_name')
    

    def __str__(self):#esta función str devolverá en el template titulo y subtitulo con queryset
        return str(self.id) + ' ' + self.name + ' ' + self.short_name 
        #el str() transforma en string lo encerrado en parentesis