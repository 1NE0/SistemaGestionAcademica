from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context, RequestContext
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,login,logout
from Academia_Arte_y_Vida.app.gestionacademica.forms import *
from Academia_Arte_y_Vida.app.gestionacademica.forms import login_form
from django.contrib.auth.decorators import login_required
from Academia_Arte_y_Vida.app.gestionacademica.models import *
from Academia_Arte_y_Vida.app.gestionacademica import models
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes, Pagos, Detalle_Pagos
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes,Pagos,Detalle_Pagos, Programas
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.

def asignaturas (request):
    asignaturasLista = Asignaturas.objects.all()
    return render(request,"asignaturas.html" , {'asignaturas' : asignaturasLista})

def cursos (request):
    cursosLista = Cursos.objects.all()
    return render(request,"cursos.html", {'cursos' : cursosLista})

def Index(request):
    # request : para realizar peticiones
    return render(request, "index.html")


@login_required(login_url='/login/login.html')
def Admision(request):
    return render(request, "Admisiones.html")


@login_required(login_url='/login/login.html')
def Programas(request):
    docente = None
    estudiante = None

    programasLista = models.Programas.objects.all()
    userID = request.user.id
    if Estudiantes.objects.get(user_id=userID) == None:
        docente = Docentes.objects.get(user_id=userID)
    
    estudiante = Estudiantes.objects.get(user_id=userID)
    inscripcionesEstudiante = Inscripciones.objects.filter(Estudiante_id = estudiante.identificacion)
    print(inscripcionesEstudiante['id'])
    
    
    

    return render(request, "programas.html", {'programasLista': programasLista , 'estudiante' : estudiante , 'docente' : docente , 'inscripciones' : inscripcionesEstudiante.values()})


login_required(login_url='/login/login.html')


def Pagos(request):
    return render(request, 'pagos.html')


@login_required(login_url='/login/login.html')
def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "CrearPrograma.html", context)


@login_required(login_url='/login/login.html')
def lista_programas(request):
    programas = models.Programas.objects.all()
    context = {'programas':programas}
    return render(request,'lista_programas.html',context)

@login_required(login_url='/login/login.html')
def editar_programa(request,cod_programa):
    programa = models.Programas.objects.get(cod_programa=cod_programa)
    if request.method == 'GET':
        form = Programas_Form(instance=programa)
    else:
        form = Programas_Form(request.POST, instance=programa)
        if form.is_valid():
            form.save()
        return redirect("../../listaprograma")
    
    context = {'form':form}

    return render(request,"CrearPrograma.html",context)

@login_required(login_url='/login/login.html')
def eliminar_programa(request,cod_programa):
    programa = models.Programas.objects.get(cod_programa=cod_programa)
    if request.method == 'POST':
        programa.delete()
        return redirect("lista_programas.html")
    context = {'programa':programa}
    return render(request,"eliminar_programa.html",context)




@login_required(login_url='/login/login.html')
def CrearAsignatura(request):
    form = Asignaturas_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "crearasignatura.html", context)


@login_required(login_url='/login/login.html')
def CrearCurso(request):
    form = Cursos_Form(request.POST or None)

    if form.is_valid():
        Codcurso = form.cleaned_data['cod_curso']
        print("aaaaaaaaaaaaaaaaa" + Codcurso)
        form.save()

    context = {'form': form}

    return render(request, "crearcurso.html", context)


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        usuario = User.objects.get(username=username)
        print("el usuario encontrado es" + usuario.username)
        boole = check_password(password , usuario.password)
        print(boole)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return render(request , "index.html" , {'user':user})
            else:
                #  Retornar a una pagina de error
                redirect('/')
    return render(request, 'login/login.html')


def logout_user(request):
    user = request.user
    logout(request)
    return render(request, "index.html")

#logica pagos#####################################################################################
def buscarEstudiante(request):

    return render(request, "buscarEstudiante.html")

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
    idestudiante = request.GET["idestudiante"]
    estuidante = Estudiantes.objects.get(identificacion=idestudiante)
    idpagos = request.GET["idpago"]
    programalabel = request.GET["programas"]
    programa1 = models.Programas.objects.get(nom_programa=programalabel)
    monto = request.GET["monto"]
    fechahoy = datetime.now()
    #prgramas = request.GET["programas"]
    p2 = models.Pagos(id=idpagos,Programa=programa1,motivo=motivo)
    print(p2)
    Dp= models.Detalle_Pagos(Estudiante=estuidante,Pagos=p2,monto=monto,Fecha=fechahoy).save()
    #return render(request,"pago#2.html",Dp="detallep",)   
    return redirect('/')



def historiaPagos(request):
    # asigno los datos de el campo a una variable
    idEstudiante = request.GET["id"]
    estudiantes = Estudiantes.objects.filter(identificacion__icontains=idEstudiante)
    buscarPago = models.Detalle_Pagos.objects.filter(Estudiante=idEstudiante)

    return render(request, "historiaPagos.html", {"buscarP": buscarPago})
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
            estudiante = form_est.save()
            correo = request.POST.get('correo')
            # OBTENER LOS DATOS DE LOGEO PARA CREAR UN USER...
            usuario = request.POST.get('usuario')
            contraseña = request.POST.get('password')
            #CODIFICAR LA CONTRASEÑA

            print(contraseña)
            # DESPUES DE CREAR EL ESTUDIANTE, DEBEMOS ASIGNARLE UN USER...
            usercito = User.objects.create_user(usuario, correo, contraseña)
            usercito.is_staff = True # El usuario puede acceder a las secciones de administración.
            usercito.set_password = contraseña
            group = Group.objects.get(name='estudiantes')
            usercito.groups.add(group)
            usercito.save()
            login(request , usercito)
            #BUSCAR EL ESTUDIANTE Y ASIGNARLE EL USUARIO
            estudiantico = Estudiantes.objects.get(identificacion=request.POST.get('identificacion'))
            estudiantico.user = usercito
            estudiantico.save()

            # AHORA DEBEMOS CREAR LA INSCRIPCION...
            print(request.POST.get('programas'))
            programaSelect = models.Programas.objects.get(cod_programa=request.POST.get('programas'))
            inscripcion = Inscripciones.objects.create(Fecha_Realizacion=datetime.now,Programa=programaSelect,Estudiante=estudiante)
            inscripcion.save()
            #inscripcion = models.Inscripciones(Fecha_Realizacion = datetime.now(), 
            #                                    Programa = request.POST.get('programas'),
            #                                    Estudiante = estudiante).save()
            
            #print(request.GET('programas'))
            return render(request,"index.html",{'form' : form_est, 'objprograma' : programas, 'form_ins' : inscripcion })
        
        return render(request,"registro/formInscripcion.html",{'form' : form_est, 'objprograma' : programas})

