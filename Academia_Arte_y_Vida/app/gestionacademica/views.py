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
from django.contrib.auth.decorators import login_required
from Academia_Arte_y_Vida.app.gestionacademica.models import *
from Academia_Arte_y_Vida.app.gestionacademica import models
from datetime import datetime,timedelta
from django.shortcuts import redirect
from django.core import serializers
from django.http import JsonResponse
import json
import reportlab
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@login_required(login_url='/login')
def estudiantes(request):
    estudiantesLista = Estudiantes.objects.all()
    return render(request, "administracion/estudiantes.html", {'estudiantes': estudiantesLista})

@csrf_protect
def periodo(request):
    csrfContext = RequestContext(request).flatten()
    programas = models.Programas.objects.all()
    periodos = models.periodo.objects.all()
    
    return render(request,"administracion/periodo.html" , {'periodos' : periodos , 'programas' : programas })

def asignaturas(request):
    asignaturasLista = Asignaturas.objects.all()
    return render(request, "asignaturas.html", {'asignaturas': asignaturasLista})


def fotos(request):
    return render(request, "fotos/fotos.html")


def cursos(request):
    cursosLista = models.Cursos.objects.all()

    return render(request, "cursos.html", {'cursos': cursosLista})

def docentes(request):
    docentesLista = models.Docentes.objects.all()
    return render(request, "administracion/docentes.html", {'docentes': docentesLista})

#def detalles_pagos(request):
#    pagosLista = models.Pagos.objects.all()
#    return render(request, "administracion/pago.html", {'detallePago': pagosLista})

def Index(request):
    # request : para realizar peticiones
    print(request.user.username)
    return render(request, "index.html")


def PDF(request):
    # request : para realizar peticiones
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def quienes_somos(request):
    return render(request, "quienesSomos.html")


def programas_info(request):
    # request : para realizar peticiones
    return render(request, "info/programas_info.html")


@login_required(login_url='/login')
def Admision(request):

    usuariosConPago = models.usuario.objects.filter(pagoRealizado=True)
    print(usuariosConPago)
    return render(request, "Admisiones.html", {'usuariosLista': usuariosConPago})

@login_required(login_url='/login')
def estadisticas(request):
    return render(request,"administracion/estadisticas.html")
@login_required(login_url='/login')
def administracion_staff(request):
    return render(request, "administracion/admin.html")

@login_required(login_url='/login')
def board_estudiante(request):
    return render(request, "board_estudiante/board.html")
@login_required(login_url='/login')
def perfil(request):
    usuario = request.user
    
    docentes = models.Docentes.objects.all()
    estudiantes = models.Estudiantes.objects.all()
    usuarios = models.usuario.objects.all()

    return render(request,"perfil/perfil.html" , {'estudiantes' : estudiantes, 'docentes' : docentes , 'usuarios' : usuarios})

    
    
#  Programas -----------------------------------------------------------


@login_required(login_url='/login')
def Programas(request):
    programasLista = models.Programas.objects.all()
    programasMatriculados = []  #guardaremos los programas que ya estan matriculados
    programasSinMatricular = []
    for programa in programasLista:
        try:
            inscripcion = models.inscripcionPrograma.objects.get(programa=programa,periodo=models.periodo.periodo_actual())
            programasMatriculados.append(programa)
        except models.inscripcionPrograma.DoesNotExist:
            programasSinMatricular.append(programa)

    return render(request, "programas.html", {'programasMatriculados': programasMatriculados , 'programasSinMatricular' : programasSinMatricular})


import random
@csrf_exempt
def asignarProgramas(request):
    listaProgramas = request.POST.getlist('listaProgramas[]') #lista de programas enviados desde ajax
    modo = "Guardado"

    for programa in listaProgramas:  #lo recorremos
        programaModel = models.Programas.objects.get(cod_programa=programa)
        #verificar si ya se encuentra registrado
        try:
            inscripcion = models.inscripcionPrograma.objects.get(programa=programa,periodo=models.periodo.periodo_actual())
            #si no sale error quiere decir que ya hay un programa matriculado
            modo = "actualizado"
        except:
            #sino guarda la inscripcion
            inscripcion = models.inscripcionPrograma.objects.create(cod_programa=programaModel,Id=random.randrange(1000000),cod_periodo=models.periodo.periodo_actual())
            inscripcion.save()

    return HttpResponse(modo)


def Pagos(request):
    return render(request, 'pagos.html')


@login_required(login_url='/login')
def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("../../listaprograma")
    context = {
        'form': form
    }

    return render(request, "CrearPrograma.html", context)


@login_required(login_url='/login')
def lista_programas(request):
    programas = models.Programas.objects.all()
    context = {'programas': programas}
    return render(request, 'lista_programas.html', context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def eliminar_programa(request, cod_programa):
    programa = models.Programas.objects.get(cod_programa=cod_programa)
    if request.method == 'POST':
        programa.delete()
        return redirect("../../listaprograma")
    context = {'programa': programa}
    return render(request, "eliminar_programa.html", context)


# Asignaturas ----------------------------------------------------------

@login_required(login_url='/login')
def CrearAsignatura(request):
    form = Asignaturas_Form(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "crearasignatura.html", context)


@login_required(login_url='/login')
def CrearCurso(request):
    #if request.is_ajax():
    form = Cursos_Form(request.POST or None)

    if form.is_valid():
        Codcurso = form.cleaned_data['cod_curso']
        print("aaaaaaaaaaaaaaaaa" + Codcurso)
        form.save()
        return redirect("../../listacursos")

    context = {'form': form}

    return render(request, "crearcurso.html", context)

def lista_curso(request):
    if request.is_ajax and request.method == "GET":
        print("soy un ajaxxx")
        print(request.GET)
        cursos = models.Cursos.objects.filter(nom_curso = request.GET.get('nombre'))
        data =  serializers.serialize('json', cursos)
        print(type(data))
        return HttpResponse(data, 'application/json') #content_type=True)
    return HttpResponse(data)

@login_required(login_url='/login')
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


@login_required(login_url='/login')
def Eliminar_Curso(request, cod_curso):
    curso = models.Cursos.objects.get(cod_curso=cod_curso)
    if request.method == 'POST':
        curso.delete()
        return redirect("../../listacursos")
    context = {'curso': curso}
    return render(request, "eliminar_curso.html", context)


def is_member(user):
    return user.groups.filter(name='director').exists()

@csrf_protect
def login_user(request):
    csrfContext = RequestContext(request).flatten()
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
            return render(request, "login/login.html", {'user': user} , csrfContext)
        print("entreeeee otraaaa vezzzzzz")
    return render(request, 'login/login.html' , csrfContext)


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


@login_required(login_url='/login')
def primerpago(request):
    usuario = models.usuario.objects.get(user=request.user.id)
    programa = models.Programas.objects.get(nom_programa=usuario.nom_programa)

    if request.POST:
        email = usuario.correo

        # stripe
        intento = stripe.PaymentIntent.create(
        amount=17*100,
        currency='usd',
        payment_method_types=['card'],
        receipt_email='seas19754@gmail.com',
        )
        stripe.PaymentIntent.confirm(
            intento["id"],
            payment_method='pm_card_visa',

        )

        redirect('index')
    return render(request,"primer_pago/primer_pago.html",{'usuario':usuario})


def pago_realizado(request):
    return render(request,"info/pago_realizado.html")


def crearPeriodo (request):


    if request.method == 'POST':   # SI ES UN POST, QUIERE DECIR QUE LE DIERON A ENVIAR FORMULARIO
        Fecha_ini = request.POST.get('Fecha_inicio')
        Fecha_fin = request.POST.get('Fecha_final')

        # GUARDÉ LA LISTA DE PERIODOS, QUE TENGAN LA MISMA FECHA
        buscarPeriodo = models.periodo.objects.filter(Fecha_inicio=Fecha_ini,Fecha_final=Fecha_fin)
        print(buscarPeriodo.exists())
        if buscarPeriodo.exists(): # SI LA LISTA NO ESTÁ VACIA QUIERE DECIR QUE HAY PERIODOS YA REGISTRADOS CON ESTAS FECHAS
            #ya hay un periodo registrado
            print("YA SE ENCONTRO ESE PERIODO BOLUDOOOOO")
            context = {'error_boludo' : 'error'}  # AQUI ARMO MI CONTEXTO CON EL ERROR
            return JsonResponse(context)   # AQUI LO RETORNO, (ESTO ES LO QUE VA A ATRAPAR EL AJAX) NOTA: EN AJAX DEBE ESTAR ESPECIFICADO (dataType: "json")
        else:
            # si no se encuentra registrado
            periodo = models.periodo(Fecha_inicio=Fecha_ini,Fecha_final=Fecha_fin)
            periodo.save()
            periodoAmandar = models.periodo.objects.get(Fecha_inicio=Fecha_ini,Fecha_final=Fecha_fin)
            context = {'registrado' : 'true', 'fecha_inicio' : periodoAmandar.Fecha_inicio,'fecha_final' : periodoAmandar.Fecha_final}
            
            return JsonResponse(context)
            
    ################ AQUI SE MANEJA LA LOGICA PARA FECHAS ########################
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.month
    dia_actual = fecha_actual.day
    if mes_actual < 9:
        mes_actual = "0"+str(mes_actual)
    if dia_actual < 9:
        dia_actual = "0"+str(dia_actual)

    ########################################
    fecha_recomendada = fecha_actual + timedelta(days=120)
    mes_recomendado = fecha_recomendada.month
    dia_recomendado = fecha_recomendada.day
    if mes_recomendado < 9:
        mes_recomendado = "0" + str(mes_recomendado)
    if dia_recomendado < 9:
        dia_recomendado = "0" + str(dia_recomendado)
    return render(request,"crearPeriodo.html",{'fecha_actual' : fecha_actual,'fecha_recomendada' : fecha_recomendada,'mes_recomendado' : mes_recomendado,'dia_recomendado':dia_recomendado,'mes_actual' : mes_actual , 'dia_actual' : dia_actual})


def borrar_periodo(request):
    pass




def activarReferenciaDePago (request):

    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        userActual = request.user
        usuario = models.usuario.objects.get(user=userActual)

        # GUARDAR LA REFERENCIA DE PAGO
        usuario.referenciaPago = codigo
        usuario.pagoRealizado = True

        print(usuario.referenciaPago)
        usuario.save()

        return render(request,"primer_pago/correcto.html")



@csrf_exempt
def aceptarUsuario(request):

    if request.method == 'POST':
        print(request.POST.get('codigoUsuario'))
        codigo = request.POST.get('codigoUsuario')  # obtener el codigo del usuario de la peticion 
        
        #buscar el usuario para volverlo un estudiante

        usuario = models.usuario.objects.get(identificacion=codigo)   # encontrar el objeto usuario con el codigo dado
        programa = models.Programas.objects.get(nom_programa=usuario.nom_programa)   # encontrar el objeto programa con el nom_programa del usuario

        # crear un estudiante con la informacion del usuario 
        estudiante = models.Estudiantes(ciudad=usuario.ciudad,identificacion=usuario.identificacion,
                                        tipo=usuario.tipo,nombres=usuario.nombres,apellidos=usuario.apellidos,edad=usuario.edad,
                                        sexo=usuario.sexo,correo=usuario.correo,telefono=usuario.telefono,direccion=usuario.direccion,user=usuario.user)


        # obtener el programa al que se quiere inscribir el estudiante en el periodo actual
        
        try:
            programaAinscribirse = models.inscripcionPrograma.objects.get(cod_programa=programa.cod_programa,cod_periodo=models.periodo.periodo_actual().codigo)
            # guardar el estudiante y borrar el usuario
            estudiante.save()
            usuario.delete()
            # crear la inscripcion estudiante con la informacion dada
            inscripcion = models.InscripcionEstudiante(periodo=models.periodo.periodo_actual(),Fecha_Realizacion=datetime.now(),cod_inscripcionPrograma=programaAinscribirse,Estudiante=estudiante)
            inscripcion.save()
        except models.inscripcionPrograma.DoesNotExist:
            print("El programa al que se quiere registrar el estudiante, no está disponible en este periodo")


        return HttpResponse("correcto")

