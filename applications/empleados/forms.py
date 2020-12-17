from django import forms

from .models import Empleados

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleados
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
            )
        widgets = {
                'habilidades': forms.CheckboxSelectMultiple()
    
            }
"""
Los formularios que son creados en este forms.py, deben ser exportados hacia 
el views.py donde se importan para despues crear un form_class y pasarle como
valor el formulario creado, cuyo fields sustituyen el fields de la vista
"""