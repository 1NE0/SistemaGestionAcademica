from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from Academia_Arte_y_Vida.app.gestionacademica.forms import *
from Academia_Arte_y_Vida.app.gestionacademica.forms import login_form


# Create your views here.

def Index(request):
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

def login_user(request):
    
    username = password = ''
    form1 = login_form()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request , user)
            return render(request , "index.html" , {'user':user})

    return render(request, 'login/login.html')


def logout_user(request):
       user = request.user
       logout(request)
       return render(request , "index.html")