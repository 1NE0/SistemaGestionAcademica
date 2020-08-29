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

from Academia_Arte_y_Vida.app.gestionacademica.views import Ejemplo
from Academia_Arte_y_Vida.app.gestionacademica.views import Admision
from Academia_Arte_y_Vida.app.gestionacademica.views import Programas, CrearPrograma
from Academia_Arte_y_Vida.app.gestionacademica.views import buscarEstudiante, buscar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ejemplo/$', Ejemplo, name="ejemplo"),
    url(r'^admisiones/$', Admision, name='admisiones'),
    url(r'^programas/$', Programas, name="programas"),
    url(r'^crearprograma/$',CrearPrograma, name="crearprograma"),
    # url(r'^pago/$',RegistroPago, name="registropago"),
    # url(r'^Dpago/$',RegDetallePago, name="Dregistropago"),
    url(r'^buscarEstudiante/$',buscarEstudiante, name="buscarestudiante"),
    url(r'^registroPago/$',buscar, name="registropago"),
    url(r'^pago/$',buscar, name="registropago"),

    
    

]
