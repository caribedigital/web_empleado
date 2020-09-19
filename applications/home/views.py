from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
#import model
from .models import Prueba
from .forms import PruebaForm


# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html' # la carpeta home esta en BASE_DIR/templates/home/prueba.html

class FoundationView(TemplateView):
    template_name = 'home/prueba_foundationzurb.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'ListaNumeros'
    queryset = ['0', '1', '10', '20', '30']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'ListaPrueba'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
    
