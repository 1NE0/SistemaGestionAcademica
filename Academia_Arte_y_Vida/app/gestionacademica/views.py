from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from django.shortcuts import render
from Academia_Arte_y_Vida.app.gestionacademica.forms import *


# Create your views here.

def Ejemplo(request):
    #request : para realizar peticiones
    return render(request,"index.html")

def Admision(request):
    return render(request, "Admisiones.html", {})

def Programas(request):
    
    return render(request, "programas.html", {})

def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()
    
    context ={
        'form':form
    }

    return render(request,"CrearPrograma.html",context)

def CrearAsignatura(request):
    form = Asignaturas_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render(request,"crearasignatura.html",context)

def CrearCurso(request):
    form = Cursos_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'form':form}

    return render(request,"crearcurso.html",context)

