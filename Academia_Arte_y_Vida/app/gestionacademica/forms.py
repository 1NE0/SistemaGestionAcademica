from django.forms import ModelForm
from Academia_Arte_y_Vida.app.gestionacademica.models import Programas, Asignaturas
from Academia_Arte_y_Vida.app.gestionacademica.models import Pagos, Detalle_Pagos
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
# #formulario para pagos#############################################################################

# class pagoFormulario(ModelForm):
#     class Meta:
#         model = Pagos
#         fields = '__all__'


# #detalle pagp formulario############################################################################
# class detalle_pagoForm(ModelForm):
#     class Meta:
#         model = Detalle_Pagos
#         fields = '__all__'