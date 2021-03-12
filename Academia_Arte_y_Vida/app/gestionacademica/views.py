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
from django.utils import tree
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


from django.core.files.storage import FileSystemStorage
# Create your views here.


def estudiantes(request):
    estudiantesLista = Estudiantes.objects.all()
    return render(request, "administracion/estudiantes.html", {'estudiantes': estudiantesLista})

@csrf_protect
def periodo(request):
    csrfContext = RequestContext(request).flatten()
    programas = models.Programas.objects.all()
    periodos = models.periodo.objects.all()
    periodoActual = models.periodo.periodo_actual()

    #programas
    programasLista = models.Programas.objects.all()
    programasMatriculados = []  #guardaremos los programas que ya estan matriculados
    programasSinMatricular = []
    for programa in programasLista:
        try:
            inscripcion = models.inscripcionPrograma.objects.get(programa=programa,periodo=models.periodo.periodo_actual())
            programasMatriculados.append(programa)
        except models.inscripcionPrograma.DoesNotExist:
            programasSinMatricular.append(programa)

    return render(request,"administracion/periodo.html" , {'periodos' : periodos , 'programas' : programas , 'periodoActual' : periodoActual , 'programasMatriculados' : programasMatriculados , 'programasSinMatricular' : programasSinMatricular})

# --------------------------------------------------------------------


@csrf_protect
def programas_Admin(request):
    programas = models.Programas.objects.all()
    
    return render(request,"administracion/programas/programas.html",{'programas':programas})



@login_required(login_url='/login')
def crearPrograma (request): 

    if request.method == "POST" and request.is_ajax:   # SI ES UN POST, QUIERE DECIR QUE LE DIERON A ENVIAR FORMULARIO        
        codigo = request.POST.get('cod_programa')
        nombre = request.POST.get('nom_programa')
        contenido = request.POST.get('contenido_Aca')
        duracion = request.POST.get('duracion')

        programa = models.Programas(cod_programa=codigo,nom_programa=nombre,contenido_Aca=contenido,duracion=duracion)

        programa.save()

        return HttpResponse("correcto")
    
    return render(request,"administracion/programas/crear.html")


def asignaturas(request):
    asignaturasLista = Asignaturas.objects.all()
    return render(request, "asignaturas.html", {'asignaturas': asignaturasLista})


def fotos(request):
    return render(request, "fotos/fotos.html")




def cursos(request):
    InscripcionesProgramasMatriculados = models.inscripcionPrograma.objects.filter(periodo=models.periodo.periodo_actual())
    periodo = models.periodo.periodo_actual()
    detalles = models.detalle_curso.objects.filter(periodo=models.periodo.periodo_actual())
    sinMatricula = []
    conMatricula = []

    for detalle in detalles:
        if detalle.Nivel_Curso.inscripcion_curso.Id_inscripcionPrograma == None:
            sinMatricula.append(detalle)
        else:
            conMatricula.append(detalle)
    
    return render(request, "cursos.html", {'programas': InscripcionesProgramasMatriculados, 'conMatricula' : conMatricula, 'sinMatricula' : sinMatricula , 'inscripcionesTotales' : detalles})

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



def Admision(request):

    usuariosConPago = models.usuario.objects.filter(pagoRealizado=True)
    print(usuariosConPago)
    return render(request, "Admisiones.html", {'usuariosLista': usuariosConPago})


def estadisticas(request):
    return render(request,"administracion/estadisticas.html")

@login_required(login_url='/login')
def administracion_staff(request):
    return render(request, "administracion/admin.html")

@login_required(login_url='/login')
def board_estudiante(request):
    return render(request, "board_estudiante/board.html")

@login_required(login_url='/login')
def board_docente(request):
    return render(request, "board_docente/panel.html")

@login_required(login_url='/login')
def perfil(request):
    usuario = request.user
    
    docentes = models.Docentes.objects.all()
    estudiantes = models.Estudiantes.objects.all()
    usuarios = models.usuario.objects.all()

    return render(request,"perfil/perfil.html" , {'estudiantes' : estudiantes, 'docentes' : docentes , 'usuarios' : usuarios})

    
    
#  Programas -----------------------------------------------------------



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
def asignarProgramas(request):  #asignar programas a periodos
    listaProgramas = request.POST.getlist('listaProgramas[]') #lista de programas enviados desde ajax
    inscripcionesRegistradas = models.inscripcionPrograma.objects.filter(periodo=models.periodo.periodo_actual())
    modo = "Guardado"
    if inscripcionesRegistradas.exists:
        for inscripcionRegistrada in inscripcionesRegistradas:
            estaContenido = False
            for programa in listaProgramas:
                if programa == inscripcionRegistrada.programa.nom_programa:
                    estaContenido = True
            if estaContenido == False:
                print("Elimine la inscripcion")
                modo = "actualizado"
                inscripcionRegistrada.delete()

    
    for programa in listaProgramas:  #lo recorremos
        programaModel = models.Programas.objects.get(cod_programa=programa)
        #verificar si ya se encuentra registrado
        try:
            inscripcion = models.inscripcionPrograma.objects.get(programa=programa,periodo=models.periodo.periodo_actual())
            #si no sale error quiere decir que ya hay un programa matriculado
            modo = "actualizado"
        except:
            #sino esta registrada, guarda la inscripcion
            
            inscripcion = models.inscripcionPrograma.objects.create(programa=programaModel,Id=random.randrange(1000000),periodo=models.periodo.periodo_actual())
            inscripcion.save()
    

    return HttpResponse(modo)


def Pagos(request):
    return render(request, 'pagos.html')



def CrearPrograma(request):
    form = Programas_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("../../listaprograma")
    context = {
        'form': form
    }

    return render(request, "CrearPrograma.html", context)


def lista_programas(request):
    programas = models.Programas.objects.all()
    context = {'programas': programas}
    return render(request, 'lista_programas.html', context)



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


def eliminar_programa(request, cod_programa):
    programa = models.Programas.objects.get(cod_programa=cod_programa)
    if request.method == 'POST':
        programa.delete()
        return redirect("../../listaprograma")
    context = {'programa': programa}
    return render(request, "eliminar_programa.html", context)


# Asignaturas ----------------------------------------------------------
"""
def CrearAsignatura(request):
    docentes = models.Docentes.objects.all()
    return render(request, "crearAsignatura.html", {'docentes' : docentes})

"""

def crudAsignatura(request):

    docentes = models.Docentes.objects.all()
    
    if request.method == "POST" and request.is_ajax:
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        docente = request.POST.get('docente')

        # buscar el docente
        docenteObj = models.Docentes.objects.get(nombres=docente)  
        asignatura = models.Asignaturas(cod_asig=codigo , nom_asig = nombre , descripcion=descripcion , Docente=docenteObj)
        
        asignatura.save()
        
        return HttpResponse("ok")

    return render(request,"crearasignatura.html",{'docentes' : docentes})


def CrearCurso(request):
    docentes = models.Docentes.objects.all()
    detalles = models.InscripcionCurso.objects.all()
    if request.method == "POST" and request.is_ajax:
        print("ENTREEEEEEEEEEE AL IF jeje")
        codigo = request.POST.get('cod_curso')
        nombre_curso = request.POST.get('nom_curso')
        nivel = request.POST.get('nivel')
        descripcion = request.POST.get('descripcion')
        docenteIdSelect = request.POST.get('docente')
        grupo = request.POST.get('grupo')
        dia = request.POST.get('dia')
        hora_inicial = request.POST.get('hora_inicial')
        hora_final = request.POST.get('hora_final')

        docente = models.Docentes.objects.get(identificacion=docenteIdSelect)
        curso = models.Cursos(cod_curso= codigo, nom_curso=nombre_curso)
        
        inscripcionCurso = models.InscripcionCurso(Id=random.randrange(0,1000000),curso = curso)

        # crear un nivel del curso
        nivelCurso = models.Nivel_Cursos(Id=random.randrange(0,1000000),nivel=nivel,descripcion=descripcion,inscripcion_curso=inscripcionCurso)
        
        #crear un detalle
        detalleCurso = models.detalle_curso(grupo=grupo,dia=dia,horaInicio=hora_inicial,horaFinal=hora_final,Nivel_Curso=nivelCurso,Docente=docente,periodo=models.periodo.periodo_actual())


        #guardar todo
        curso.save()
        inscripcionCurso.save()
        nivelCurso.save()
        detalleCurso.save()
        return HttpResponse("correcto")
    
    return render(request, "crearcurso.html", {'docentes' : docentes , 'detalles' : detalles})

def lista_curso(request):
    if request.is_ajax and request.method == "GET":
        print("soy un ajaxxx")
        print(request.GET)
        cursos = models.Cursos.objects.filter(nom_curso = request.GET.get('nombre'))
        data =  serializers.serialize('json', cursos)
        print(type(data))
        return HttpResponse(data, 'application/json') #content_type=True)
    return HttpResponse("valido")


@csrf_protect
def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
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
            try:
                user = models.User.objects.get(username=username)
                # si lo encuentra quiere decir que el problema está en la contraseña
                return HttpResponse("contraseñaIncorrecta")
            except User.DoesNotExist:
                # no está registrado
                return HttpResponse("usuarioNoExiste")
        
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
    return HttpResponse("activo")

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
    tipos = []

    for tipoTupla in models.Estudiantes.tipos_doc:
            tipos.append(tipoTupla[1])
    
    print(tipos)
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
        verificarUsuarioRepetido = models.User.objects.get(username=usuario)
        if verificarUsuarioRepetido != None:
            return HttpResponse ("Usuario Repetido")
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

    return render(request, "registro/formInscripcion.html", {'form': form_est, 'programas': programas, 'departamentos': departamentos, 'ciudades': ciudades , 'tiposDocumentos' : tipos})

def registrarInscripcion(request):
    print("entre al registrarInscripcion")
    identificacion = request.POST.get('identificacion')
    tipoDocumento = request.POST.get('tipoDocumento')
    nombres = request.POST.get('nombres')
    apellidos = request.POST.get('apellidos')
    edad = request.POST.get('edad')
    genero = request.POST.get('genero')
    programa = request.POST.get('programa')
    ciudad = request.POST.get('ciudad')
    departamento = request.POST.get('departamento')
    direccion = request.POST.get('departamento')
    telefono = request.POST.get('telefono')
    correo = request.POST.get('correo')

    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    #CREAR EL USUARIO DE LOGEO
    try:
        verificarUsuarioRepetido = models.User.objects.get(username=username)
        print("soy un usuario repetido")
        return HttpResponse("Username ya usado")
    except User.DoesNotExist:
        usercito = User.objects.create_user(username, correo, password)

    # PERMISOS DEL USER
    usercito.is_staff = False
    usercito.set_password = password
    group = Group.objects.get(name='usuarios')
    usercito.groups.add(group)

    # OBTENER EL PROGRAMA QUE SELECCIONO
    print(request.POST.get('programa'))
    programaSelect = models.Programas.objects.get(nom_programa=programa)

    # OBTENER LA CIUDAD QUE SELECCIONÓ
    ciudadSelect = models.ciudad.objects.get(nombre=ciudad)
    # OBTENER EL DEPARTAMENTO QUE SELECCIONÓ
    departamentoSlect = models.departamento.objects.get(nombre=departamento)
    ciudadSelect.departamento = departamentoSlect
    #CREAR EL USUARIO CON TODA LA INFORMACION
    usuarioRegistrado = models.usuario(identificacion=identificacion
                                        ,tipo=tipoDocumento
                                        ,nombres=nombres
                                        ,apellidos=apellidos
                                        ,edad=edad
                                        ,sexo=genero
                                        ,correo=correo
                                        ,telefono=telefono
                                        ,direccion=direccion
                                        ,user=usercito
                                        ,ciudad=ciudadSelect
                                        ,nom_programa=programaSelect.nom_programa)
    print(usuarioRegistrado.nombres)
    usercito.save()
    login(request, usercito)
    usuarioRegistrado.save()
    
    #enviar correo
    #enviarCorreo("sebastian" , "juan.ortiz.alzate@correounivalle.edu.co" , "una pruebita")


    return HttpResponse("correcto")

################### CRUD DOCENTE #####################

def crearDocente(request):

    docentes = models.Docentes.objects.all()
    ciudades = models.ciudad.objects.all()
    tipos = []

    for tipo in models.Docentes.tipos_doc:
        tipos.append(tipo[1])

    if request.method == "POST" and request.is_ajax:
        print("ENTREEEEEEEEEEE AL IF jeje")

        tipoDocumento = request.POST.get('tipoDocumento')
        identificacion = request.POST.get('id')
        nombres = request.POST.get('nombres')
        apellidos =request.POST.get('apellidos')
        edad = request.POST.get('edad')
        genero = request.POST.get('genero')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        
        correoElectronico = request.POST.get('correo')
        username = request.POST.get('username')
        password = request.POST.get('password')

        #CREAR EL USUARIO DE LOGEO
        try:
            verificarUsuarioRepetido = models.User.objects.get(username=username)
            print("Usuario repetido")
            return HttpResponse("Username ya usado")
        except User.DoesNotExist:
            usercito = User.objects.create_user(username, correoElectronico, password)

        usercito.is_staff = False
        usercito.set_password = password
        grupo = Group.objects.get(name = 'docentes')
        usercito.groups.add(grupo)

        ciudadSeleccionada = models.ciudad.objects.get(nombre = ciudad)

        docenteAñadido = models.Docentes(identificacion=identificacion,
                                        tipo=tipoDocumento,
                                        nombres=nombres,
                                        apellidos=apellidos,
                                        edad=edad,
                                        sexo= genero,
                                        correo=correoElectronico,
                                        telefono=telefono,
                                        direccion=direccion,
                                        user = usercito,
                                        ciudad = ciudadSeleccionada)

        usercito.save()
        docenteAñadido.save()
        return HttpResponse("correcto")

    return render(request, "administracion/docentes.html", {'docentes': docentes,'ciudades': ciudades, 'tiposDocs': tipos})

def lista_docente(request):
    
    if request.is_ajax:
        print("SOY AJAXX")
        print(request.GET)
        docentes = models.Docentes.objects.filter(nombres = request.GET.get('nombre'))
        data =  serializers.serialize('json', docentes)
        print(type(data))
        return HttpResponse(data)
    return HttpResponse("activo")

#############################################

@login_required(login_url='/login')
def primerpago(request):       # no se està utilizando
    usuario = models.usuario.objects.get(user=request.user.id)
    return render(request,"primer_pago/primer_pago.html",{'usuario':usuario})


def pago_realizado(request):
    return render(request,"info/pago_realizado.html")


def crearPeriodo (request):


    if request.method == 'POST':   # SI ES UN POST, QUIERE DECIR QUE LE DIERON A ENVIAR FORMULARIO
        codigo = random.randrange(1000000)

        try:
            periodoVerificar = models.periodo.objects.get(codigo=codigo)
        except models.periodo.DoesNotExist:
            codigo += 1
        
        Fecha_ini = request.POST.get('Fecha_inicio')
        Fecha_fin = request.POST.get('Fecha_final')

        # GUARDÉ LA LISTA DE PERIODOS, QUE TENGAN LA MISMA FECHA
        buscarPeriodo = models.periodo.objects.filter(codigo=codigo,Fecha_inicio=Fecha_ini,Fecha_final=Fecha_fin)
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
            programaAinscribirse = models.inscripcionPrograma.objects.get(programa=programa.cod_programa,periodo=models.periodo.periodo_actual().codigo)
            # guardar el estudiante y borrar el usuario
            group = Group.objects.get(name='estudiantes')
            estudiante.user.groups.add(group)
            estudiante.save()
            usuario.delete()
            # crear la inscripcion estudiante con la informacion dada
            inscripcion = models.InscripcionEstudiante(periodo=models.periodo.periodo_actual(),Fecha_Realizacion=datetime.now(),cod_inscripcionPrograma=programaAinscribirse,Estudiante=estudiante)
            inscripcion.save()
        except models.inscripcionPrograma.DoesNotExist:
            print("El programa al que se quiere registrar el estudiante, no está disponible en este periodo")
            return HttpResponse("Incorrecto")


        return HttpResponse("correcto")


@csrf_exempt
def editarEstudiante(request):   #abrir el modal

    if request.method == 'POST':
        print("estoy en POST")
        identificacion = request.POST.get('estudiante')
        print(identificacion)
        estudianteActual = models.Estudiantes.objects.get(identificacion=identificacion)
        return render(request, "editarEstudiante.html", {'estudiante' : estudianteActual})
    return render(request,"editarEstudiante.html")


def modalEditarEstudiante(request):    # logica de editar el estudiante
    print(request.POST.get('identificacion'))

    estudianteModificado = models.Estudiantes.objects.get(identificacion=request.POST.get('identificacion'))

    estudianteModificado.nombres = request.POST.get('nombres')
    estudianteModificado.apellidos = request.POST.get('apellidos')
    estudianteModificado.edad = request.POST.get('edad')
    estudianteModificado.sexo = request.POST.get('sexo')
    estudianteModificado.correo = request.POST.get('correo')
    estudianteModificado.telefono = request.POST.get('telefono')
    estudianteModificado.direccion = request.POST.get('direccion')

    estudianteModificado.save();
    return HttpResponse("correcto")

@csrf_exempt
def eliminarEstudiante(request):
    identificacion = request.POST.get('estudiante[]')
    estudiante = models.Estudiantes.objects.get(identificacion=identificacion)
    estudiante.delete()
    return HttpResponse("eliminado")

def pagos(request):
    return render(request,"pagos.html")

#    BOARD DEL ESTUDIANTE

def programasEstudiante(request):
    return render(request, "board_estudiante/programasEstudiante.html")

def asignaturasEstudiante(request):
    return render(request, "board_estudiante/asignaturasEstudiante.html")

def pagosEstudiante(request):
    return render(request, "board_estudiante/pagosEstudiante.html")




#    BOARD DEL DOCENTE
@csrf_exempt
def cursosDocente(request):
    user = models.User.objects.get(id=request.user.id)
    docente = models.Docentes.objects.get(user=user)
    cursos = models.detalle_curso.objects.filter(Docente=docente)
    
    if request.method == 'POST':
        id_detalle = request.POST['detalle']
        detalle = models.detalle_curso.objects.get(id=id_detalle)
        archivo = request.FILES['documento']
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        actividad = models.actividades(file=archivo,titulo=titulo,descripcion=descripcion,detalle_curso=detalle.id)
        actividad.save()


        return HttpResponse("correcto")
    return render(request, "board_docente/cursosDocente.html" , {'docente' : docente , 'cursos' : cursos})


def asignaturasDocente(request):
    return render(request, "board_docente/asignaturasDocente.html")

    


@csrf_exempt
def verificarUsername(request):
    user = request.POST.get('username')
    
    try:
        usuario = models.User.objects.get(username=user)
        return HttpResponse("noDisponible")
    except models.User.DoesNotExist:
        return HttpResponse("disponible")

@csrf_exempt
def verificarIdentificacion(request):
    identificacion = request.POST.get('identificacion')

    try:
        usuario = models.usuario.objects.get(identificacion=identificacion)
        return HttpResponse("noDisponible")
    except models.usuario.DoesNotExist:
        try:
            estudiante = models.Estudiantes.objects.get(identificacion=identificacion)
            return HttpResponse("noDisponible")
        except models.Estudiantes.DoesNotExist:
            return HttpResponse("disponible")




from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def enviarCorreo(name,email,message):

    body = {
                'name': name,
                'email': email,
                'message': message,
            }
        

    email_message = EmailMessage(
            subject='Mensaje de usuario',
            body=body,
            from_email=email,
            to=['seas19754@gmail.com'],
        )
    email_message.content_subtype = 'html'
    email_message.send()


@csrf_exempt
def obtenerEstadisticas(request):
    estudiantesMatriculados = models.Estudiantes.objects.all().count()
    programasTotales = models.Programas.objects.all().count()
    usuariosTotales = models.usuario.objects.all().count()
    cursosTotales = models.Cursos.objects.all().count()
    asignaturasTotales = models.Asignaturas.objects.all().count()
    docentesTotales = models.Docentes.objects.all().count()

    periodosTotales = models.periodo.objects.all()
    
    arreglo = { 'estudiantesCantidad' : estudiantesMatriculados , 'programasTotales' : programasTotales , 'usuariosTotales' : usuariosTotales , 'cursosTotales' : cursosTotales , 'asignaturasTotales' : asignaturasTotales , 'docentesTotales' : docentesTotales}
    data = json.dumps(arreglo)


    
    return JsonResponse(data,safe=False)


@csrf_exempt
def guardarCursoPrograma(request):

    inscripcionCursos = request.POST.getlist('listaCursos[]')
    programa = request.POST.get('programa')  # obtener la inscripcion del programa
    # AGREGAR A ESTA INSCRIPCION, TODOS LOS CURSOS
    programaInscripcion = models.inscripcionPrograma.objects.get(Id=programa)

    # BORRAR LAS INSCRIPCIONES PARA VOLVERLAS A GUARDAR (ES COMO ACTUALIZAR)    
    for inscripcion in models.InscripcionCurso.objects.filter():
        if inscripcion.Id_inscripcionPrograma == programaInscripcion:
            inscripcion.Id_inscripcionPrograma = None
            inscripcion.save()


    # HACER LA RELACION DE LA INSCRIPCION CURSO, CON LA INSCRIPCION PROGRAMA
    for inscripcion in inscripcionCursos:
        print(inscripcion)
        inscripcionC = models.InscripcionCurso.objects.get(Id=inscripcion)
        inscripcionC.Id_inscripcionPrograma = programaInscripcion
        inscripcionC.save()
    
    return HttpResponse('Perfecto')

    