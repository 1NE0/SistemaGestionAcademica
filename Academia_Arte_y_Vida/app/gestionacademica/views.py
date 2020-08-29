from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from django.shortcuts import render
from Academia_Arte_y_Vida.app.gestionacademica.forms import Programas_Form
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes#se importa los modelos para poder usarlo en la busqueda
from Academia_Arte_y_Vida.app.gestionacademica import models
from datetime import datetime #fechas
# from Academia_Arte_y_Vida.app.gestionacademica.forms import pagoFormulario, detalle_pagoForm
# from django.views.generic import CreateView
# from Academia_Arte_y_Vida.app.gestionacademica.models import Detalle_Pagos

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
        

