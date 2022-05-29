from calendar import c
from winreg import DeleteValue
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import http
from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12354)
    curso.save()
    texto=f"------>Curso: {curso.nombre} Comision: {curso.comision}"

    return HttpResponse(texto)
def inicio(request):
    return render(request,'AppCoder/inicio.html')

def profesores(request):
    profesores=Profesor.objects.all()
    return render(request, 'AppCoder/profesores.html',{'profesores':profesores})

def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')

def cursos(request):
    return render(request,'AppCoder/cursos.html')

def entregables(request):
    return render(request,'AppCoder/entregables.html')

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso=Curso(nombre=informacion['nombre'],comision=informacion['comision'])  
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'AppCoder/cursos.html', {'formulario':miFormulario})
    
def busquedaComision(request):
    return render(request,'AppCoder/busquedaComision.html')

def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/ResultadosBusqueda.html',{'cursos':cursos, 'comision':comision})
    else:
        respuesta = "No se ingresó ninguna comision"
        return render(request, 'AppCoder/ResultadosBusqueda.html', {'respuesta':respuesta})

def eliminarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, 'AppCoder/profesores.html',{'profesores':profesores})

def editarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = ProfeFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            #Muestro lista de profes de nuevo
            profesores=Profesor.objects.all()
            return render(request, 'AppCoder/profesores.html',{'profesores':profesores})
    else:
        miFormulario=ProfeFormulario(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,'email':profesor.email,'profesion':profesor.profesion})
    return render(request,'AppCoder/editarProfesor.html',{'formulario':miFormulario, 'nombre':nombre})

class EstudianteList(ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes.html'

class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre','apellido','email']

class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre','apellido','email']

class EstudianteBorrar(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre','apellido','email']