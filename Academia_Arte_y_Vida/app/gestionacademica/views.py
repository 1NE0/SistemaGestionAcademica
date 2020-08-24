from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.template import Template, Context, RequestContext
from django.shortcuts import render
from Academia_Arte_y_Vida.app.gestionacademica.forms import Programas_Form

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
"""
def Login_Academico(request):
    
    return render(request,"login.html",context)
    """