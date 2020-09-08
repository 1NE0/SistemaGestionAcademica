from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context , RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from Academia_Arte_y_Vida.app.gestionacademica.forms import *
from Academia_Arte_y_Vida.app.gestionacademica.forms import login_form
from django.contrib.auth.decorators import login_required
from Academia_Arte_y_Vida.app.gestionacademica.models import *
from Academia_Arte_y_Vida.app.gestionacademica import models
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes,Pagos,Detalle_Pagos, Programas
from datetime import datetime
from django.shortcuts import redirect

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

login_required(login_url='/login/login.html')
def Pagos(request):
    return render(request, 'pagos.html')

@login_required(login_url='/login/login.html')
def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()
    
    context ={
        'form':form
    }

    return render(request,"CrearPrograma.html",context)

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
        Codcurso = form.cleaned_data['cod_curso']
        print("aaaaaaaaaaaaaaaaa" + Codcurso)
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
        print(user.id)
        if user is not None:
            login(request , user)
            estudiante = Estudiantes.objects.get(user_id=user.id)
            return render(request , "index.html" , {'user':user , 'estudiante':estudiante})

    return render(request, 'login/login.html')


def logout_user(request):
       user = request.user
       logout(request)
       return render(request , "index.html")



#logica pagos#####################################################################################
def buscarEstudiante(request):


    return render(request,"buscarEstudiante.html")

def buscar(request):
    if request.GET["id"]:
       idEstudiante = request.GET["id"] #asigno los datos de el campo a una variable
       estudiantes=Estudiantes.objects.filter(identificacion__icontains=idEstudiante)
       programas=models.Programas.objects.all()
       motivo = models.Pagos.objects.filter(motivo__icontains='1')
       buscarPago=models.Detalle_Pagos.objects.filter(Estudiante=idEstudiante)
       fechaActual = datetime.now()
       return render(request,"registrarpago.html",{"buscarP":buscarPago,"programaobj":programas,"Estudianteobj":estudiantes, "fechaActual":fechaActual, "query":idEstudiante , "motivo":motivo})
    else:
        mensaje="no se ingresaron datos"

    return HttpResponse(mensaje) #objeto http 

def agregarpago(request):
    
    motivo = request.GET["motivos"]
    idestudiante = request.GET["idestudiante"]
    estuidante= Estudiantes.objects.get(identificacion=idestudiante)
    idpagos = request.GET["idpago"]
    programalabel = request.GET["programas"]
    programa1=models.Programas.objects.get(nom_programa=programalabel)
    monto = request.GET["monto"]
    fechahoy = datetime.now()
    #prgramas = request.GET["programas"]
    p = Pagos(id=idpagos, Programa=programa1,motivo=motivo)
    p1 = Pagos(Programa=programa1,id=idpagos,motivo=motivo).save()
    Dp=Detalle_Pagos(Estudiante=estuidante,Pagos=p1,monto=monto,Fecha=fechahoy).save()
    #return render(request,"pago#2.html",Dp="detallep",)   
    return redirect('/')


def historiaPagos(request):
    idEstudiante = request.GET["id"] #asigno los datos de el campo a una variable        
    estudiantes = Estudiantes.objects.filter(identificacion__icontains=idEstudiante)
    buscarPago=models.Detalle_Pagos.objects.filter(Estudiante=idEstudiante)

    return render(request,"historiaPagos.html",{"buscarP":buscarPago})

############################# Inscripcion Academica #######################################

def crearInscripcion(request):
        programas = models.Programas.objects.all()
        form_est = form_Estudiante(request.POST)
        

        if form_est.is_valid():
            print (request.POST.get('identificacion'))
            # GUARDAMOS EL ESTUDIANTE
            estudiante = form_est.save()

            # OBTENER LOS DATOS DE LOGEO PARA CREAR UN USER...
            usuario = request.POST.get('usuario')
            contraseña = request.POST.get('password')
            # DESPUES DE CREAR EL ESTUDIANTE, DEBEMOS ASIGNARLE UN USER...
            usercito = User.objects.create_user(usuario, contraseña)
            usercito.is_staff = True # El usuario puede acceder a las secciones de administración.
            usercito.save()
            
            #BUSCAR EL ESTUDIANTE Y ASIGNARLE EL USUARIO
            estudiantico = Estudiantes.objects.get(identificacion=request.POST.get('identificacion'))
            estudiantico.user = usercito
            estudiantico.save() 

            # AHORA DEBEMOS CREAR LA INSCRIPCION...
            print(request.POST.get('programas'))
            programaSelect = models.Programas.objects.get(nom_programa=request.POST.get('programas'))
            inscripcion = Inscripciones.objects.create(Fecha_Realizacion=datetime.now,Programa=programaSelect,Estudiante=estudiante)
            inscripcion.save()
            
            #print(request.GET('programas'))
            return render(request,"index.html",{'form' : form_est, 'objprograma' : programas, 'form_ins' : inscripcion })
        
        return render(request,"registro/formInscripcion.html",{'form' : form_est, 'objprograma' : programas})

