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
    url(r'^programas/$', Programas, name="programas"),
    url(r'^cursos/$', cursos, name="cursos"),
    url(r'^asignaturas/$', asignaturas, name="asignaturas"),
    url(r'^pagos/$', Pagos, name="pagos"),
    url(r'^crearprograma/$', CrearPrograma, name="crearprograma"),
    url(r'^listaprograma/$', lista_programas, name="listaprograma"),
    url(r'^editarprograma/(?P<cod_programa>\w+)/$',
        editar_programa, name="editarprograma"),
    url(r'^eliminarprograma/(?P<cod_programa>\w+)/$',
        eliminar_programa, name="eliminarprograma"),
    url(r'^crearasignatura/$', CrearAsignatura, name="crearasignatura"),
    url(r'^crearcurso/$', CrearCurso, name="crearcurso"),
    url(r'^listacursos/$', lista_curso, name="listacursos"),
    url(r'^editarcurso/(?P<cod_curso>\w+)$', Editar_curso, name="editarcurso"),
    url(r'^eliminarcurso/(?P<cod_curso>\w+)$',
        Eliminar_Curso, name="eliminarcurso"),
    url(r'^login/$', login_user, name="login"),
    url(r'^logout/$', logout_user, name="logout"),
    url(r'^registroPago/$', buscar, name="reguistropago"),
    url(r'^buscarestudiante/$', buscarEstudiante, name="buscarestudiante"),
    url(r'^pago/$', agregarpago, name="pago"),
    url(r'^historiaPago/$', historiaPagos, name="historiapago"),
    url(r'^registro/formInscripcion/$', crearInscripcion, name="crearinscripcion"),
    url(r'^primerpago/$', primerpago, name="primerpago"),
    url(r'^estudiantes/$', estudiantes, name="estudiantes"),
    url(r'^estadisticas/$', estadisticas, name="estadisticas"),
    url(r'^quienes_somos/$', quienes_somos, name="quienes_somos"),
    url(r'^informacion_programas/$', programas_info, name="programas_info"),
    url(r'^administracion/$', administracion_staff, name="administracion"),
    url(r'^board_estudiante/$', board_estudiante, name="board_estudiante"),
    url(r'^inscripcion/$', primerpago, name="inscripcion"),
    url(r'^docentes/$', docentes, name="docentes"),
    #url(r'^pago/$', detalles_pagos, name="pago")
    url(r'^fotos/$', fotos, name="fotos"),
    url(r'^perfil/$', perfil, name="perfil"),
    url(r'^periodos/$', periodo, name="periodos"),
    url(r'^crearPeriodo$', crearPeriodo, name="crearPeriodo"),
]
