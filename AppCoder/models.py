from tkinter import N
from xml.dom import NoModificationAllowedErr
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return "Nombre:" +(self.nombre)+" Apellido: "+str(self.apellido)+" Email: "+(self.email)

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

    def __str__(self):
        return "Nombre:" +(self.nombre)+" Apellido: "+str(self.apellido)+" Email: "+(self.email)+" Profesion: "+(self.profesion)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True,blank = True) 