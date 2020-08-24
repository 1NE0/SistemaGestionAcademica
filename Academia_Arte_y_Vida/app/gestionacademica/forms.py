from django.forms import ModelForm
from Academia_Arte_y_Vida.app.gestionacademica.models import Programas, Asignaturas
from django.contrib.auth.models import User

class Programas_Form(ModelForm):
    class Meta:
        model = Programas
        fields = '__all__'
"""
class Asignaturas_Form(ModelForm):
    class Meta:
        model = Asignaturas
        fields = '__all__'

class Login_Academico(ModelForm):
    class Meta:
        model = User
        fields = {
            'username',
            'password'
        }
"""