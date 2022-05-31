from calendar import c
from winreg import DeleteValue
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import http
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12354)
    curso.save()
    texto=f"------>Curso: {curso.nombre} Comision: {curso.comision}"

    return HttpResponse(texto)
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,'AppCoder/inicio.html',{'url':avatares[0].imagen.url})

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
@login_required
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

class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_list.html'

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

#-----LOGIN----------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,'AppCoder/inicio.html',{'usuario':usuario,'mensaje':'Bienvenido'})
            else:
                return render(request,'AppCoder/inicio.html',{'mensaje':'USUARIO INCORRECTO, VUELVA A INTENTARLO'})
        else:
            return render(request,'AppCoder/inicio.html',{'mensaje':'LOS DATOS INGRESADOS NO SON VÁLIDOS. VUELVA A INTENTARLO'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppCoder/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'AppCoder/inicio.html',{'mensaje':f'Usuario: {username} creado de manera exitosa.'})
        else:
            return render(request, 'AppCoder/inicio.html',{'mensaje':'NO SE PUDO CREAR EL USUARIO'})
    else:
        form = UserRegistrationForm()
        return render(request,'AppCoder/register.html',{'form':form})
@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'AppCoder/inicio.html',{'usuario':usuario,'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request,'AppCoder/editarPerfil.html',{'formulario':formulario,'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.imagen):
                avatarViejo.delete()
            imagen=Avatar(user=user, imagen=formulario.cleaned_data['avatar'])
            imagen.save()
            return render(request,'AppCoder/inicio.html',{'usuario':user,'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppCoder/agregarAvatar.html',{'formulario':formulario,'usuario':user})