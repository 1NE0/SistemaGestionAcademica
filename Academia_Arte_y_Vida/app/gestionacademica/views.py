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
from django.core import serializers
from django.http import JsonResponse
import json
from django.contrib import messages
# Create your views here.


@login_required(login_url='/login/login.html')
def estudiantes(request):
    estudiantesLista = models.Estudiantes.objects.all()
    # if request.is_ajax and request.method == "GET":
    #     instancia = serializers.serialize('json', estudiantesLista)
    #     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #     # send to client side.
    #     return JsonResponse({"instance": instancia})
    print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    return render(request, "estudiantes/estudiantes.html", {'estudiantes': estudiantesLista})


def asignaturas(request):
    asignaturasLista = Asignaturas.objects.all()
    return render(request, "asignaturas.html", {'asignaturas': asignaturasLista})


def fotos(request):
    return render(request, "fotos/fotos.html")


def cursos(request):
    cursosLista = Cursos.objects.all()
    return render(request, "cursos.html", {'cursos': cursosLista})


def Index(request):
    # request : para realizar peticiones
    print(request.user.username)
    return render(request, "index.html")


def quienes_somos(request):
    # request : para realizar peticiones
    return render(request, "quienesSomos.html")


def programas_info(request):
    # request : para realizar peticiones
    return render(request, "info/programas_info.html")


@login_required(login_url='/login/login.html')
def Admision(request):

    usuariosRegistrados = models.usuario.objects.all()

    return render(request, "Admisiones.html", {'usuariosLista': usuariosRegistrados})


def administracion_staff(request):
    return render(request, "administracion/admin.html")


def board_estudiante(request):
    return render(request, "board_estudiante/board.html")

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
                # if is_member(user):
                #     return render(request, "administracion/admin.html", {'user': user})
                # Redirect to a success page.
                return render(request, "index.html", {'user': user})
        else:
            #  Retornar a una pagina de error
            print("entreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return render(request, "login/login.html", {'user': user})
        print("entreeeee otraaaa vezzzzzz")
    return render(request, 'login/login.html')


def logout_user(request):
    user = request.user
    logout(request)
    return render(request, "index.html")


def buscarEstudiante(request):
    if request.is_ajax:
        print("soy un ajax")
        estudiantes = models.Estudiantes.objects.filter(nombres=request.GET.get('nombre'))
        data = serializers.serialize('json' , estudiantes)
        print(data)
        # return HttpResponse(data)
        return  HttpResponse(data, 'application/json')
    return HttpResponse(data)

#logica pagos#####################################################################################


def buscar(request):
    if request.GET["id"]:
        # asigno los datos de el campo a una variable
        idEstudiante = request.GET["id"]
        estudiantes = Estudiantes.objects.filter(
            identificacion__icontains=idEstudiante)
        programas = models.Programas.objects.all()
        buscarPago = models.Detalle_Pagos.objects.filter(
            Estudiante=idEstudiante)
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
    p3 = models.Pagos(Programa=programa1,
                      id=request.GET["idpago"], motivo=motivo)
    p3.save()
    DetlleP = models.Detalle_Pagos(
        Estudiante=estuidante, Pagos=p3, monto=monto, Fecha=fechahoy)
    DetlleP.save()
    return redirect('/')


def historiaPagos(request):
    # asigno los datos de el campo a una variable
    idEstudiante = request.GET["id"]
    estudiantes = Estudiantes.objects.filter(
        identificacion__icontains=idEstudiante)
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
    form_est = form_Estudiante_nuevo(request.POST)
    departamentos = models.departamento.objects.all()
    ciudades = models.ciudad.objects.all()

    if form_est.is_valid():
        print(request.POST.get('identificacion'))
        # GUARDAMOS EL USUARIO (estudiante sin registrarse)
        estudiante_nuevo = form_est.save(commit=False)

        # OBTENER LOS DATOS DE LOGEO PARA CREAR UN USER...
        correo = request.POST.get('correo')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('password')
        # CODIFICAR LA CONTRASEÑA
        print(contraseña)
        # CREAR UN USER PARA LOGEARSE
        usercito = User.objects.create_user(usuario, correo, contraseña)
        # El usuario puede acceder a las secciones de administración.
        usercito.is_staff = False
        usercito.set_password = contraseña
        group = Group.objects.get(name='usuarios')
        usercito.groups.add(group)
        # INICIAR SESION CON ESTE USER
        login(request, usercito)

        # OBTENER EL PROGRAMA QUE SELECCIONO
        print(request.POST.get('programas'))
        programaSelect = models.Programas.objects.get(
            nom_programa=request.POST.get('programas'))
        usuarioCreado = models.ciudad(
            codigo=1234, nombre="florida_machete_y_cuchillo")

        # OBTENER LA CIUDAD QUE SELECCIONÓ
        ciudadSelect = models.ciudad.objects.get(
            nombre=request.POST.get('ciudades_combo'))

        estudiante_nuevo.ciudad = ciudadSelect
        estudiante_nuevo.save()
        # BUSCAR EL USUARIO REGISTRADO ANTERIORMENTE Y ASIGNARLE EL USER DE LOGEO
        usuarioCreado = models.usuario.objects.get(
            identificacion=request.POST.get('identificacion'))
        usuarioCreado.user = usercito
        usuarioCreado.nom_programa = programaSelect.nom_programa
        usuarioCreado.ciudad = ciudadSelect

        # GUARDAR TODOOO
        usercito.save()
        usuarioCreado.save()

        # LLEVARLO A LA PAGINA DE PAGO EN LINEA
        # return primerpago(request)
        messages.success(request, '¡Usuario creado Satisfactoriamente!')
        return render(request, "index.html")

    return render(request, "registro/formInscripcion.html", {'form': form_est, 'objprograma': programas, 'objdepartamentos': departamentos, 'objciudades': ciudades})


@login_required(login_url='/login/login.html')
def primerpago(request):
    usuario = models.usuario.objects.get(user=request.user.id)
    programa = models.Programas.objects.get(nom_programa=usuario.nom_programa)

    print(models.periodo.periodo_actual().Fecha_final.month)
    if request.method == "POST":
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # TRANSFORMAR EL USUARIO EN ESTUDIANTE
        estudiante = models.Estudiantes(ciudad=usuario.ciudad, identificacion=usuario.identificacion, tipo=usuario.tipo, nombres=usuario.nombres, apellidos=usuario.apellidos,
                                        edad=usuario.edad, sexo=usuario.sexo, correo=usuario.correo, telefono=usuario.telefono, direccion=usuario.direccion, user=usuario.user)
        estudiante.programa = programa
        # AGREGARLO AL GRUPO "ESTUDIANTES"
        group = Group.objects.get(name='estudiantes')
        request.user.groups.add(group)
        # GUARDAR EL ESTUDIANTE
        estudiante.save()
        # BORRAR EL USUARIO
        usuario.delete()

        # CREAR LA INSCRIPCION
        inscripcion = Inscripciones(Estudiante=estudiante, periodo=periodo.periodo_actual(
        ), Fecha_Realizacion=datetime.now(), Programa=programa)
        inscripcion.save()

    return render(request, "primer_pago/primer_pago.html", {'usuario': usuario})
