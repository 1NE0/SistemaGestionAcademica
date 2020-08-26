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
from django.urls import path #
from django.conf.urls import url

from Academia_Arte_y_Vida.app.gestionacademica.views import *


urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', Index, name="index"),
    url(r'^admisiones/$', Admision, name='admisiones'),
    url(r'^programas/$', Programas, name="programas"),
    url(r'^crearprograma/$',CrearPrograma, name="crearprograma"),
    url(r'^crearasignatura/$',CrearAsignatura, name="crearasignatura"),
    url(r'^crearcurso/$',CrearCurso, name="crearcurso"),
    url(r'^login/$', login_user, name="login")

]
