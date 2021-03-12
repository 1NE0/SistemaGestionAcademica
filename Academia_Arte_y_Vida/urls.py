"""Academia_Arte_y_Vida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from Academia_Arte_y_Vida import settings
from Academia_Arte_y_Vida.app.gestionacademica.views import *


urlpatterns = [

    url(r'^$', Index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', Index, name="index"),
    url(r'^admisiones/$', Admision, name='admisiones'),
    #url(r'^programas/$', Programas, name="programas"),
    url(r'^cursos/$', cursos, name="cursos"),
    url(r'^asignaturas/$', asignaturas, name="asignaturas"),
    url(r'^pagos/$', Pagos, name="pagos"),
    #url(r'^crearprograma/$', CrearPrograma, name="crearprograma"),
    url(r'^listaprograma/$', lista_programas, name="listaprograma"),
    url(r'^editarprograma/(?P<cod_programa>\w+)/$',
        editar_programa, name="editarprograma"),
    url(r'^eliminarprograma/(?P<cod_programa>\w+)/$',
        eliminar_programa, name="eliminarprograma"),
   # url(r'^crearasignatura$', CrearAsignatura, name="crearAsignatura"),
    url(r'^crearcurso/$', CrearCurso, name="crearcurso"),
    url(r'^listacursos/$', lista_curso, name="listacursos"),
    url(r'^login/$', login_user, name="login"),
    url(r'^logout/$', logout_user, name="logout"),
    url(r'^registroPago/$', buscar, name="reguistropago"),
    url(r'^buscarestudiante/$', buscarEstudiante, name="buscarestudiante"),
    url(r'^pago/$', agregarpago, name="pago"),
    url(r'^historiaPago/$', historiaPagos, name="historiapago"),
    url(r'^registro/formInscripcion/$', crearInscripcion, name="crearinscripcion"),
    url(r'^registrarInscripcion/$', registrarInscripcion, name="registrarInscripcion"),
    url(r'^primerpago/$', primerpago, name="primerpago"),
    url(r'^estudiantes/$', estudiantes, name="estudiantes"),
    url(r'^quienes_somos/$', quienes_somos, name="quienes_somos"),
    url(r'^informacion_programas/$', programas_info, name="programas_info"),
    url(r'^administracion/$', administracion_staff, name="administracion"),
    url(r'^inscripcion/$', primerpago, name="inscripcion"),
    url(r'^docentes/$', docentes, name="docentes"),
    url(r'^crearDocente/$', crearDocente, name="crearDocente"),
    url(r'^listaDocente/$', lista_docente, name="listaDocente"),
    #url(r'^pago/$', detalles_pagos, name="pago")
    url(r'^fotos/$', fotos, name="fotos"),
    url(r'^perfil/$', perfil, name="perfil"),
    url(r'^periodos/$', periodo, name="periodos"),
    url(r'^pago_realizado/$', pago_realizado, name="pago_realizado"),
    url(r'^crearPeriodo$', crearPeriodo, name="crearPeriodo"),
    #Programas
    url(r'^programas/$', programas_Admin, name="programas"),
    url(r'^programas/crear$', crearPrograma, name="crearprograma"),
    
    url(r'^efectuarReferencia$',activarReferenciaDePago, name="referenciaPago"),
    url(r'^aceptarUsuario$', aceptarUsuario, name="aceptarUsuario"),
    url(r'^asignarProgramas$', asignarProgramas, name="asignarProgramas"),
    url(r'^editarEstudiante$', editarEstudiante, name="editarEstudiante"),
    url(r'^pagos$', pagos, name="pagos"),
    url(r'^verificarUser/$', verificarUsername, name="verificarUsername"),
    url(r'^verificarIdentificacion/$', verificarIdentificacion, name="verificarIdentificacion"),
    url(r'^modificarEstudiante$', modalEditarEstudiante, name="modificarEstudiante"),
    url(r'^eliminarEstudiante$', eliminarEstudiante, name="eliminarEstudiante"),
    url(r'^crudAsignatura$', crudAsignatura, name="crudAsignatura"),
 
    # board estudiante
    url(r'^board_estudiante/$', board_estudiante, name="board_estudiante"),
    url(r'^programasEstudiante$', programasEstudiante, name="programasEstudiante"),
    url(r'^asignaturasEstudiante$', asignaturasEstudiante, name="asignaturasEstudiante"),
    url(r'^pagosEstudiante$', pagosEstudiante, name="pagosEstudiante"),

    # board docente
    url(r'^board_docente/$', board_docente, name="board_docente"),
    url(r'^cursosDocente$', cursosDocente, name="cursosDocente"),
    url(r'^asignaturasDocente$', asignaturasDocente, name="asignaturasDocente"),


    #estadisticas
    url(r'^obtenerEstadisticas$', obtenerEstadisticas, name="obtenerEstadisticas"),
    url(r'^estadisticas/$', estadisticas, name="estadisticas"),

    #guardar cursos en programas
    url(r'^guardarCursoPrograma/$', guardarCursoPrograma, name="guardarCursoPrograma"),
    
]
