import imp
from lib2to3.pygram import pattern_grammar
from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio,name='inicio'),
    path('profesores/',profesores,name='profesores'),
    path('estudiantes/',estudiantes,name='estudiantes'),
    path('cursos/',cursos,name='cursos'),
    path('entregables/',entregables,name='entregables'),
    path('creaCurso/',curso),
    #path('cursosFormulario/',cursosFormulario,name='cursosFormulario'),
    path('busquedaComision',busquedaComision,name='busquedaComision'),
    path('buscar',buscar,name='buscar'),
    path('eliminarProfesor/<nombre>',eliminarProfesor,name='eliminarProfesor'),
    path('editarProfesor/<nombre>',editarProfesor,name='editarProfesor'),
    path('estudiante/list/',EstudianteList.as_view(), name='estudiante_listar'),
    path('estudiante/<pk>',EstudianteDetalle.as_view(),name='estudiante_detalle'),
    path('estudiante/nuevo/',EstudianteCreacion.as_view(),name='estudiante_crear'),
    path('estudiante/editar/<pk>',EstudianteEdicion.as_view(),name='estudiante_editar'),
    path('estudiante/borrar/<pk>',EstudianteBorrar.as_view(),name='estudiante_borrar'),
    path('login',login_request,name='login'),
    path('register',register,name="register"),
    path('logout', LogoutView.as_view(template_name="AppCoder/logout.html"), name='logout')

]
