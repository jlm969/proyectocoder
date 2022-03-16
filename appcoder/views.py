from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso, Profesor, Estudiante, Entregable

# Create your views here.
def curso(self,nombre,camada):

    curso = Curso(nombre, camada)
    curso.save()
    documento = f"----->Curso: {curso.nombre}    Camada: {curso.camada} " 

    return HttpResponse(documento)

def estudiante(self, id_estudiante, nombre, apellido, email):
    
    estudiante = Estudiante(id_estudiante, nombre, apellido, email)
    estudiante.save()
    documento = f"----->ID_Estudiante: {estudiante.id_estudiante}  Nombre:{estudiante.nombre}  Apellido: {estudiante.apellido}  EMAIL: {estudiante.email}" 

    return HttpResponse(documento)    

def profesor(self, id_profesor, nombre, apellido, email, profesion):
    
    profesor = Profesor(id_profesor, nombre, apellido, email, profesion)
    profesor.save()
    documento = f"----->ID_Profesor: {profesor.id_profesor}  Nombre:{profesor.nombre}  Apellido: {profesor.apellido}  EMAIL: {profesor.email} Profesion:{profesor.profesion}" 

    return HttpResponse(documento)

def entregable(self, id_entregable, nombre, fecha_entrega, entregado):
    
    entregable = Entregable(id_entregable, nombre, fecha_entrega, entregado)
    entregable.save()
    documento = f"----->ID_Entregable: {entregable.id_entregable}  Nombre:{entregable.nombre}  Fecha_Entrega: {entregable.fecha_entrega}  Entregado: {entregable.entregado}" 

    return HttpResponse(documento)