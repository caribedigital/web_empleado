from django.contrib import admin
from .models import Empleados, Habilidades

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):#muestra estas tablas en el administrador
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name', #este campo no existe en el modelo le creamos una función.
        'id', #siempre el ultimo atributo de la lista debe cerrar en coma.
    )

    def full_name (self, obj):#imprime en una ultima columna el nombre completo
        #toda la operación
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name 

    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = ('departamento','job', 'habilidades',) #crea un campo de busqueda
    filter_horizontal = ('habilidades',) # crea un cuadro con todos los objetos almacenados en esta tabla

admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Habilidades)