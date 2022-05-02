import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio),
    path('profesores/',profesores),
    path('estudiantes/',estudiantes),
    path('cursos/',cursos),
    path('entregables/',entregables),
    path('creaCurso/',curso),
]
