from django.forms import ModelForm , Form
from django import forms
from Academia_Arte_y_Vida.app.gestionacademica import models
from Academia_Arte_y_Vida.app.gestionacademica.models import *
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
        labels = {
            
        }
        widgets = {
            'cod_asig': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_asig':forms.TextInput(attrs={'class': 'form-control'}),
            'contenido_academico': forms.Textarea(attrs={'class': 'form-control'})
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class periodo_form(ModelForm):
    class Meta:
        model = periodo
        fields = "Fecha_inicio","Fecha_final"
        widgets = {
            'Fecha_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'Fecha_final': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            # 'Fecha_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            # 'Fecha_final': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class Cursos_Form(ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'
        labels = {
            'cod_curso' : 'Codigo',
            'nom_curso' : 'Nombre',
        }
        widgets = {
            'cod_curso': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_curso': forms.TextInput(attrs={'class': 'form-control'})
        }


class nivelCurso_form(ModelForm):
    class Meta:
        model = Nivel_Cursos
        fields = ('nivel', 'descripcion')
        labels = {
            'nivel': 'Nivel',
            'descripcion' : 'Contenido del Curso',
            #'cod_Docente': 'Docente Encargado'
        }
        widgets = {
            'nivel': forms.Select(attrs={'class': 'form-control'}, choices=[('op1','1'), ('op2','2'), ('op3','3'), ('op4','4')]),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }



class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class  form_Estudiante_nuevo(ModelForm):
    class Meta:
        model = usuario
        fields = ('tipo','identificacion'  , 'nombres' , 'apellidos' , 'edad' , 'sexo' , 'correo' , 'telefono' , 'direccion')
        labels = {
            'tipo' : 'Tipo de Documento',
            'identificacion' : 'Identificacion',
            'nombres' : 'Nombres',
            'apellidos' : 'Apellidos',
            'edad': 'Edad',
            'sexo' : 'Genero',
            'correo' : 'Correo Electronico',
            'telefono' : 'Telefono',
            'Direccion' : 'Direccion',
        }
        widgets = {
            'tipo' : forms.Select(attrs={'class': 'form-control'}, choices=('tipos_doc')),
            'identificacion' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombres' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo' : forms.RadioSelect(attrs=None, choices=('sexos')),
            'correo' : forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control'}),
        }


