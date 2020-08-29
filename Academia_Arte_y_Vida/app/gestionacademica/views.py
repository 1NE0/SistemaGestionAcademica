from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context , RequestContext
from django.shortcuts import render
from Academia_Arte_y_Vida.app.gestionacademica.forms import Programas_Form
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes#se importa los modelos para poder usarlo en la busqueda
from Academia_Arte_y_Vida.app.gestionacademica import models
from datetime import datetime #fechas
# from Academia_Arte_y_Vida.app.gestionacademica.forms import pagoFormulario, detalle_pagoForm
# from django.views.generic import CreateView
# from Academia_Arte_y_Vida.app.gestionacademica.models import Detalle_Pagos

from django.contrib.auth import authenticate,login,logout
from Academia_Arte_y_Vida.app.gestionacademica.forms import *
from Academia_Arte_y_Vida.app.gestionacademica.forms import login_form
from django.contrib.auth.decorators import login_required
from Academia_Arte_y_Vida.app.gestionacademica.models import *
from Academia_Arte_y_Vida.app.gestionacademica import models
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes
# Create your views here.

def Index(request):
    #request : para realizar peticiones
    return render(request,"index.html")

@login_required(login_url='/login/login.html')
def Admision(request):
    return render(request, "Admisiones.html")

@login_required(login_url='/login/login.html')
def Programas(request):
    programasLista = models.Programas.objects.all()
    return render(request, "programas.html", {'programasLista' : programasLista})

@login_required(login_url='/login/login.html')
def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()
    
    context ={
        'form':form
    }

    return render(request,"CrearPrograma.html",context)




def buscarEstudiante(request):


    return render(request,"buscarEstudiante.html")

def buscar(request):
    if request.GET["id"]:
       idEstudiante = request.GET["id"] #asigno los datos de el campo a una variable
       estudiantes=Estudiantes.objects.filter(identificacion__icontains=idEstudiante)
       programas=models.Programas.objects.all()
       buscarPago=models.Detalle_Pagos.objects.filter(Estudiante=idEstudiante)
       fechaActual = datetime.now()
       return render(request,"registrarpago.html",{"buscarP":buscarPago,"programaobj":programas,"Estudianteobj":estudiantes, "fechaActual":fechaActual, "query":idEstudiante})
    else:
        mensaje="no se ingresaron datos"

    return HttpResponse(mensaje) #objeto http 

def agregarpago(request):
    motivo = request.GET["motivos"]
    idpago = request.GET["idpago"]
    programalabel = request.GET["programa"]
    monto = request.GET["monto"]
    fechahoy = request.GET["fechaActual"]
    prgramas = request.GET["programas"]
        

@login_required(login_url='/login/login.html')
def CrearAsignatura(request):
    form = Asignaturas_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render(request,"crearasignatura.html",context)

@login_required(login_url='/login/login.html')
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
        estudiante = Estudiantes.objects.get(user_id=user.pk)
        if user is not None:
            login(request , user)

            return render(request , "index.html" , {'user':user , 'estudiante':estudiante})

    return render(request, 'login/login.html')


def logout_user(request):
       user = request.user
       logout(request)
       return render(request , "index.html")
