from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
#models
from .models import Empleados #parametro de la vista generica ListView
#forms
from .forms import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
    template_name = 'empleados/inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 10
    ordering = 'first_name'
    #no tiene declarado un context_object_name por eso se utiliza en el template un object_list directo

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleados.objects.filter(
            full_name__icontains=palabra_clave  #filtramos por el nombre
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    #no tiene declarado un context_object_name por eso se utiliza en el template un object_list directo
    model = Empleados


class ListByAreaEmpleados(ListView):
    #lista empleado de un area
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleados.objects.filter( #filtra los empleados por departamentos con shortname
        departamento__short_name = area
    )
        return lista

class ListEmpleadoByKword(ListView):
    #lista empleado por palabra clave
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('***********************')
        palabra_clave = self.request.GET.get("kword", ' ')
        lista = Empleados.objects.filter(
        first_name = palabra_clave  #filtramos por el nombre
    )
        print('lista resultado: ', lista)
        return lista

class EmpleadoDetailView(DetailView):
    model = Empleados
    template_name = "empleados/detail_empleado.html"

    #declaramos un metodo de vista generica detailview
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del Mes'
        return context
        

class ListHabilidadesEmpleados(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleados.objects.get(id=10)
        return empleado.habilidades.all()  


class SuccessView(TemplateView):#esta vista se crea solo para redirigir
    template_name = "empleados/success.html" #esta llamada en el urls con el name 'correcto'

class EmpleadosCreateView(CreateView):
    template_name = 'empleados/add.html'
    model = Empleados
    #fields = ['first_name', 'other_name', 'last_name', 'job', 'departamento', 'avatar', 'habilidades', 'hoja_vida' ]
    #puede declararse el fields de manera completa como arriba o simplemente:
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)#pendiente de este argumento
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadosCreateView, self).form_valid(form)

class SuccessUpdate(TemplateView):#esta vista se crea solo para redirigir
    template_name = "empleados/success_update.html" #esta llamada en el urls con el name 'correcto'

class EmpleadoUpdateView(UpdateView):
    template_name = 'empleados/update.html'
    model = Empleados
    fields = [
        'first_name',
        'other_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    
    ]
    success_url = reverse_lazy('empleados_app:empleados_admin') #redirige a este template despues de actualizar

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***************METODO POST*******************')
        print('***************METODO POST*******************')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('***************METODO FORM_VALID*******************')
        print('***************METODO FORM_VALID*******************')       
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class SuccessDelete(TemplateView):#esta vista se crea solo para redirigir
    template_name = "empleados/success_delete.html"     

class EmpleadoDeleteView(DeleteView):
    template_name = 'empleados/delete.html'
    model = Empleados
    success_url = reverse_lazy('empleados_app:empleados_admin')
