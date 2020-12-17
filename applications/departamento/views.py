from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView #esta vista generica esta un nivel mas abajo de las otras por eso debemos entrar en edit 
from .forms import NewDepartamentoForm
from applications.empleados.models import Empleados
from .models import Departamento

# Create your views here.

class DepartamentoListView(ListView):
     template_name = "departamento/listadpto.html"
     model = Departamento
     context_object_name = 'departamentos'
   
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamentos_app:nuevo_departamento')

    def form_valid(self, form):
        print('*******estamos en el form_valid*******')

        dpto = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name1']
        )
        dpto.save()#esta función almacena en modelo o bd Departamento

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleados.objects.create( # Modelo Empleados con esta función objects.create creamos el registro en ese modelo
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=dpto # recibe por valor lo almacenado en la instancia dpto
        
        )
        return super(NewDepartamentoView, self).form_valid(form)
