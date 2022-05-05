import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio,name='inicio'),
    path('profesores/',profesores,name='profesores'),
    path('estudiantes/',estudiantes,name='estudiantes'),
    path('cursos/',cursos,name='cursos'),
    path('entregables/',entregables,name='entregables'),
    path('creaCurso/',curso),
    #path('cursosFormulario/',cursosFormulario,name='cursosFormulario'),
    path('busquedaComision',busquedaComision,name='busquedaComision'),
    path('buscar',buscar,name='buscar')
]
