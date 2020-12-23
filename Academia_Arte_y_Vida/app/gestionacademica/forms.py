from django.forms import ModelForm , Form
from django import forms
from Academia_Arte_y_Vida.app.gestionacademica import models
from Academia_Arte_y_Vida.app.gestionacademica.models import Estudiantes,Inscripciones,Programas, Asignaturas, Cursos , usuario
from django.contrib.auth.models import User

class Programas_Form(ModelForm):
    class Meta:
        model = Programas
        fields = '__all__'
        labels = {
            'cod_programa' : 'Código',
            'nom_programa' : 'Nombre',
            'contenido_Aca': 'Contenido'
        }

class Asignaturas_Form(ModelForm):
    class Meta:
        model = Asignaturas
        fields = '__all__'
"""
class Horario_Form(ModelForm):
    class Meta:
        model = Horarios
        fields = '__all__'
        widgets = {
            
        }
"""
class Cursos_Form(ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'
        labels = {
            'cod_curso' : 'Codigo',
            'nom_curso' : 'Nombre',
            'grupo' : 'Grupo',
            'h_inicio':'Hora de inicio',
            'h_final' : 'Hora final'

        }
        widgets = {
            
        }


class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class  form_Estudiante(ModelForm):
    class Meta:
        model = usuario
        fields = ('identificacion', 'tipo' , 'nombres' , 'apellidos' , 'edad' , 'sexo' , 'correo' , 'telefono')
        labels = {
            'identificacion' : 'Identificacion',
            'tipo' : 'Tipo de Documento',
            'nombres' : 'Nombres',
            'apellidos' : 'Apellidos',
            'edad': 'Edad',
            'sexo' : 'Genero',
            'correo' : 'Correo Electronico',
            'telefono' : 'Telefono',
        }
        widgets = {
            'identificacion' : forms.TextInput(attrs={'class': 'form-control'}),
            'tipo' : forms.Select(attrs={'class': 'form-control'}, choices=('tipos_doc')),
            'nombres' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo' : forms.RadioSelect(attrs=None, choices=('sexos')),
            'correo' : forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class form_Inscripcion(ModelForm):
    class Meta:
        model = Inscripciones
        fields = [
            'Programa'
        ]
        