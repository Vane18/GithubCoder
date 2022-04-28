from calendar import c
from django import http
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12354)
    curso.save()
    texto=f"------>Curso: {curso.nombre} Comision: {curso.comision}"

    return HttpResponse(texto)