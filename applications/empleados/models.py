from django.db import models
from applications.departamento.models import Departamento #ForeignKey campo departamento se vincula con otro modelo
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    
    def __str__(self):#esta función str devolverá habilidad
        return str(self.id) + ' ' + self.habilidad
        #el str() transforma en string lo encerrado en parentesis
        


class Empleados(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'ABOGADO'),
        ('4', 'OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    other_name = models.CharField('Otro Nombre', max_length=60, blank=True, null=True)#prueba mia
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres Completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)#este atributo o campo viene del modelo Departamento de la app del mismo nombre
    avatar = models.ImageField('Foto', upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vida = RichTextField()  #ckeditor activado y llamado en esta linea para esta tabla

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):#esta función str devolverá en el template titulo y subtitulo con queryset
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name 
        #el str() transforma en string lo encerrado en parentesis, significa que el valor en los 3 campos son str