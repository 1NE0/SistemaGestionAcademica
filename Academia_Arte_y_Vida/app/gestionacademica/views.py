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
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes,Pagos,Detalle_Pagos
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
        estudiante = Estudiantes.objects.get(user_id=user.pk)
        if user is not None:
            login(request , user)

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

#class crearInscripcion(CreateView):
#    model = Inscripciones
#    programas = models.Programas.objects.all()
#    form_class_insc = form_Inscripcion
#    form_class_est = form_Estudiante
    
    #asignamos el contexto
#    def get_context_data(self, **kwargs):
#        context = super(crearInscripcion, self).get_context_data(**kwargs), {'objprograma': programas}
        #mandamos los formularios al contexto
#        if 'formIns' not in context:
#            context['formIns'] = self.form_class_insc(self.request.GET)
#        if 'formEst' not in context:
#            context['formEst'] = self.form_class_est(self.request.GET)
#        return context
    # sobreescribimos el post
#    def post(self, request): # *args, **kwargs
#        self.object = self.get_object
        # recogemos de los 2 formularios, la info que estoy ingresando
#        formIns = self.form_class_insc(request.POST)
#        formEst = self.form_class_est(request.POST)
        #validamos para poderlos guardar
#        if formIns.is_valid() and formEst.is_valid():
            # creamos una variable que me guarda el primer request.POST (form)
#            inscripcion = formIns.save(commit=False) # el commit es para que no se guarde hasta que verifique mi estudiante
#            inscripcion.estudiante = formEst.save() # con esto, creamos la relacion y guardamos los valores del form_est
#            inscripcion.save()

#            return HttpResponseRedirect(self.get_success_url())
#        else:
#            return self.render_to_response(self.get_context_data(formIns=formIns, formEst=formEst)) # me trae los formularios en blanco 

def crearInscripcion(request):
        programas = models.Programas.objects.all()
        form_est = form_Estudiante(request.POST)
        
        if form_est.is_valid():
            print (request.POST.get('identificacion'))
            # GUARDAMOS EL ESTUDIANTE
            form_est.save()

            # OBTENER LOS DATOS DE LOGEO PARA CREAR UN USER...
            usuario = request.POST.get('usuario')
            contraseña = request.POST.get('password')
            # DESPUES DE CREAR EL ESTUDIANTE, DEBEMOS ASIGNARLE UN USER...
            
            # AHORA DEBEMOS CREAR LA INSCRIPCION...
            return render(request,"index.html",{'form' : form_est})
        
        return render(request,"registro/formInscripcion.html",{'form' : form_est})

