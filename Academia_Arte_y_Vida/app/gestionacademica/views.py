from django.contrib.auth.models import Group
from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context, RequestContext
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from Academia_Arte_y_Vida.app.gestionacademica.forms import *
from Academia_Arte_y_Vida.app.gestionacademica.forms import login_form
from django.contrib.auth.decorators import login_required
from Academia_Arte_y_Vida.app.gestionacademica.models import *
from Academia_Arte_y_Vida.app.gestionacademica import models
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes, Pagos, Detalle_Pagos
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes, Pagos, Detalle_Pagos, Programas
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.

@login_required(login_url='/login/login.html')
def estudiantes(request):
    estudiantesLista = models.Estudiantes.objects.all()
    return render(request, "estudiantes/estudiantes.html", {'estudiantes': estudiantesLista})

def asignaturas(request):
    asignaturasLista = Asignaturas.objects.all()
    return render(request, "asignaturas.html", {'asignaturas': asignaturasLista})


def cursos(request):
    cursosLista = Cursos.objects.all()
    return render(request, "cursos.html", {'cursos': cursosLista})


def Index(request):
    # request : para realizar peticiones
    return render(request, "index.html")


@login_required(login_url='/login/login.html')
def Admision(request):

    usuariosRegistrados = models.usuario.objects.all()

    return render(request, "Admisiones.html", {'usuariosLista': usuariosRegistrados})


#  Programas -----------------------------------------------------------

@login_required(login_url='/login/login.html')
def Programas(request):
    docente = None
    estudiante = None
    # lists
    temp = []
    listaInscripciones = []

    programasLista = models.Programas.objects.all()
    usercito = request.user
    # mirar si el usercito esta en el grupo de estudiantes
    group = Group.objects.get(name='estudiantes')
    users = group.user_set.all()
    for user in users:
        if user.id == usercito.id:
            # si está el
            estudiante = Estudiantes.objects.get(user_id=usercito.id)
            inscripcionesEstudiante = Inscripciones.objects.filter(
                Estudiante_id=estudiante.identificacion)
            programas = [v['Programa_id']
                         for v in inscripcionesEstudiante.values()]
            return render(request, "programas.html", {'programasLista': programasLista, 'estudiante': estudiante, 'inscripcionesEstudiante': programas})

    # mirar si el usercito esta en el grupo de estudiantes
    group = Group.objects.get(name='director')
    users = group.user_set.all()
    for user in users:  # recorrer todos los users que estan en el grupo "director"
        if user.id == usercito.id:
            return render(request, "programas.html", {'programasLista': programasLista})

    return render(request, "inscripciones.html", {'programasLista': programasLista})


login_required(login_url='/login/login.html')


def Pagos(request):
    return render(request, 'pagos.html')


@login_required(login_url='/login/login.html')
def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("../../listaprograma")
    context = {
        'form': form
    }

    return render(request, "CrearPrograma.html", context)


@login_required(login_url='/login/login.html')
def lista_programas(request):
    programas = models.Programas.objects.all()
    context = {'programas': programas}
    return render(request, 'lista_programas.html', context)


@login_required(login_url='/login/login.html')
def editar_programa(request, cod_programa):
    programa = models.Programas.objects.get(cod_programa=cod_programa)
    if request.method == 'GET':
        form = Programas_Form(instance=programa)
    else:
        form = Programas_Form(request.POST, instance=programa)
        if form.is_valid():
            form.save()
        return redirect("../../listaprograma")

    context = {'form': form}

    return render(request, "CrearPrograma.html", context)


@login_required(login_url='/login/login.html')
def eliminar_programa(request, cod_programa):
    programa = models.Programas.objects.get(cod_programa=cod_programa)
    if request.method == 'POST':
        programa.delete()
        return redirect("../../listaprograma")
    context = {'programa': programa}
    return render(request, "eliminar_programa.html", context)


# Asignaturas ----------------------------------------------------------

@login_required(login_url='/login/login.html')
def CrearAsignatura(request):
    form = Asignaturas_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "crearasignatura.html", context)


# Cursos ------------------------------------------------------------------

@login_required(login_url='/login/login.html')
def CrearCurso(request):
    form = Cursos_Form(request.POST or None)

    if form.is_valid():
        Codcurso = form.cleaned_data['cod_curso']
        print("aaaaaaaaaaaaaaaaa" + Codcurso)
        form.save()
        return redirect("../../listacursos")

    context = {'form': form}

    return render(request, "crearcurso.html", context)


@login_required(login_url='/login/login.html')
def lista_curso(request):
    cursos = models.Cursos.objects.all()
    context = {'cursos': cursos}
    return render(request, "lista_cursos.html", context)


@login_required(login_url='/login/login.html')
def Editar_curso(request, cod_curso):
    curso = models.Cursos.objects.get(cod_curso=cod_curso)
    if request.method == 'GET':
        form = Cursos_Form(instance=curso)
    else:
        form = Cursos_Form(request.POST, instance=curso)
        if form.is_valid():
            form.save()
        return redirect("../../listacursos")

    context = {'form': form}

    return render(request, "crearcurso.html", context)


@login_required(login_url='/login/login.html')
def Eliminar_Curso(request, cod_curso):
    curso = models.Cursos.objects.get(cod_curso=cod_curso)
    if request.method == 'POST':
        curso.delete()
        return redirect("../../listacursos")
    context = {'curso': curso}
    return render(request, "eliminar_curso.html", context)


def is_member(user):
       return user.groups.filter(name='director').exists()

def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        # usuario = User.objects.get(username=username)
        # print("el usuario encontrado es" + usuario.username)
        # boole = check_password(password, usuario.password)

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)

                # REDIRECCIONAR AL DIRECTOR
                if is_member(user):
                    return render(request, "administracion/admin.html", {'user': user})
                # Redirect to a success page.
                return render(request, "index.html", {'user': user})
        else:
            #  Retornar a una pagina de error
            print("entreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return render(request, "login/login.html" , {'user': user})
        print("entreeeee otraaaa vezzzzzz")
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
        # asigno los datos de el campo a una variable
        idEstudiante = request.GET["id"]
        estudiantes = Estudiantes.objects.filter(identificacion__icontains=idEstudiante)
        programas = models.Programas.objects.all()
        buscarPago = models.Detalle_Pagos.objects.filter(Estudiante=idEstudiante)
        fechaActual = datetime.now()
        return render(request, "registrarpago.html", {"buscarP": buscarPago, "programaobj": programas, "Estudianteobj": estudiantes, "fechaActual": fechaActual, "query": idEstudiante})
    else:
        mensaje = "no se ingresaron datos"

    return HttpResponse(mensaje)  # objeto http


def agregarpago(request):
    motivo = request.GET["motivos"]
    idestudiante = request.GET["idestudiante"]
    estuidante = Estudiantes.objects.get(identificacion=idestudiante)
    idpagos = request.GET["idpago"]
    programalabel = request.GET["programas"]
    programa1 = models.Programas.objects.get(nom_programa=programalabel)
    monto = request.GET["monto"]
    fechahoy = datetime.now()
    p3 = models.Pagos(Programa=programa1,id=request.GET["idpago"], motivo=motivo)
    p3.save()
    DetlleP = models.Detalle_Pagos(Estudiante=estuidante, Pagos=p3, monto=monto, Fecha=fechahoy)
    DetlleP.save()
    return redirect('/')


def primerpago(request):
    if request.GET["ident"]:
      id = request.GET["ident"]
      nuevo= models.usuario.objects.get(identificacion= id)
      nuevoE = models.Estudiantes(nombres=nuevo.nombres,apellidos=nuevo.apellidos,user=nuevo.user,identificacion=nuevo.identificacion,tipo=nuevo.tipo,edad=nuevo.edad,sexo=nuevo.sexo,correo=nuevo.correo,telefono=nuevo.telefono)
      
      nuevoE.save()
      nuevo.delete()

      return render(request, "buscarEstudiante_primerpago.html",{"query": id, "idestudiante":nuevoE})
    else:
        mensaje = "no se ingresaron datos"

    return HttpResponse(mensaje)


def historiaPagos(request):
    # asigno los datos de el campo a una variable
    idEstudiante = request.GET["id"]
    estudiantes = Estudiantes.objects.filter(identificacion__icontains=idEstudiante)
    buscarPago = models.Detalle_Pagos.objects.filter(Estudiante=idEstudiante)

    return render(request, "historiaPagos.html", {"buscarP": buscarPago})


register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()

# inscripcioooon -----------------------------------------------------------------------------

def crearInscripcion(request):
    programas = models.Programas.objects.all()
    form_est = form_Estudiante(request.POST)

    if form_est.is_valid():
        print(request.POST.get('identificacion'))
        # GUARDAMOS EL ESTUDIANTE
        usuarioEstudiante = form_est.save()
        correo = request.POST.get('correo')
        # OBTENER LOS DATOS DE LOGEO PARA CREAR UN USER...
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('password')
        # CODIFICAR LA CONTRASEÑA

        print(contraseña)
        # CREAR UN USER PARA LOGEARSE
        usercito = User.objects.create_user(usuario, correo, contraseña)
        # El usuario puede acceder a las secciones de administración.
        usercito.is_staff = True
        usercito.set_password = contraseña
        group = Group.objects.get(name='usuarios')
        usercito.groups.add(group)
        # GUARDAR EL USER
        
        # INICIAR SESION CON ESTE USER
        login(request, usercito)

        # OBTENER EL PROGRAMA QUE SELECCIONO
        print(request.POST.get('programas'))
        programaSelect = models.Programas.objects.get(nom_programa=request.POST.get('programas'))
        # BUSCAR EL USUARIO REGISTRADO ANTERIORMENTE Y ASIGNARLE EL USER DE LOGEO
        usuarioCreado = models.usuario.objects.get(identificacion=request.POST.get('identificacion'))
        usuarioCreado.user = usercito
        usuarioCreado.nom_programa = programaSelect.nom_programa
        

        # inscripcion = models.Inscripciones(Fecha_Realizacion = datetime.now(),
        #                                    Programa = request.POST.get('programas'),
        #                                    Estudiante = estudiante).save()

        # GUARDAR TODOOO
        usercito.save()
        usuarioCreado.save()
        return render(request, "index.html", {'form': form_est, 'objprograma': programas})

    return render(request, "registro/formInscripcion.html", {'form': form_est, 'objprograma': programas})
