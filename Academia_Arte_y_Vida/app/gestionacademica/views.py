from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from django.shortcuts import render

# Create your views here.

def Ejemplo(request):
    #request : para realizar peticiones
    return render(request,"index.html")

def Admision(request):
    return render(request, "Admisiones.html", {})

def Programas(request):
    return render(request, "programas.html", {})
