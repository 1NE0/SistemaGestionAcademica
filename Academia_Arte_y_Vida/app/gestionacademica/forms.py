from django.forms import ModelForm
from Academia_Arte_y_Vida.app.gestionacademica.models import Programas, Asignaturas
from Academia_Arte_y_Vida.app.gestionacademica.models import Pagos, Detalle_Pagos
from django import forms
from Academia_Arte_y_Vida.app.gestionacademica.models import Programas, Asignaturas, Cursos
from django.contrib.auth.models import User


class Programas_Form(ModelForm):
    class Meta:
        model = Programas
        fields = '__all__'

class Asignaturas_Form(ModelForm):
    class Meta:
        model = Asignaturas
        fields = '__all__'

class Cursos_Form(ModelForm):
    class Meta:
        model = User
        fields = {
            'username',
            'password'
        }





class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
