from django.contrib import admin
from django.urls import path
from . import views


app_name = "empleados_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name = 'empleados_all'
    ),
    path(
        'empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(),
        name = 'empleados_admin'
    ),
    path(
        'listar-by-area/<shortname>/', 
        views.ListByAreaEmpleados.as_view(),
        name = 'area_empleados'
        ),
    path(
        'buscar-empleados/',
        views.ListEmpleadoByKword.as_view()
        ),
    path('listar-habilidades-empleados/', views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
        ),
    path(
        'add-empleado/', 
        views.EmpleadosCreateView.as_view(),
        name='empleado_add'
        ),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path(
        'update-empleado/<pk>', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
        ),
    path(
        'success2/', 
        views.SuccessUpdate.as_view(), 
        name='correcto2'
        ),
    path(
        'delete-empleado/<pk>', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
        ),
    path(
        'success3/', 
        views.SuccessDelete.as_view(), 
        name='correcto3'
        ),
]
