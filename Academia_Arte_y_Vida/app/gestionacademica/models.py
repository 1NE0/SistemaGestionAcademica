from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# periodo ############################################################################################################


class periodo(models.Model):
    Fecha_inicio = models.DateField(default="")
    Fecha_final = models.DateField(default="")

    def periodo_actual():
        return periodo.objects.last()


class departamento(models.Model):
    cod_dpto = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)


class ciudad(models.Model):
    codigo = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)

#clase Estudiante######################################################################################################


class Estudiantes(models.Model):
    tipos_doc = (
        ('1', 'Cedula Ciudadania'), ('2', 'Tarjeta de identidad'), ('3',
                                                                    'Cedula de Extranjeria'), ('4', 'Certificado Cabildo '), ('5', 'Pasaporte'),
    )
    identificacion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=tipos_doc, default='2')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField(blank=False)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    correo = models.EmailField(blank=False)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(default="",max_length=60, blank=False)
    # hacer la relacion a user
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ciudad = models.ForeignKey(
        ciudad, default="", null=True, blank=False, on_delete=models.CASCADE)


#clase programa########################################################################################################
class Programas(models.Model):
    cod_programa = models.CharField(primary_key=True, max_length=10)
    nom_programa = models.CharField(max_length=30)
    contenido_Aca = models.CharField(max_length=500)
    periodo = models.ForeignKey(
        periodo, default="", null=False, blank=False, on_delete=models.CASCADE)
    #Asignatura = models.ForeignKey(Asignaturas,null=True,blank=True,on_delete=models.CASCADE)
    # FALTA

    def _str_(self):
        return "{0}".format(self.nom_programa)
    #     return "({0}) {1} Curso(s) = {2}, Asignatura(s) = {3}".format(self.cod_programa,self.nom_programa)

#clase inscripcion####################################################################################################


class Inscripciones(models.Model):
    class Meta:
        unique_together = (('Programa', 'Estudiante'),)

    Fecha_Realizacion = models.DateTimeField(auto_now_add=True)
    Programa = models.ForeignKey(
        Programas, null=False, blank=False, on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(
        Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    periodo = models.ForeignKey(
        periodo, default="", null=False, blank=False, on_delete=models.CASCADE)

#Docentes ###############################################################################################################


class Docentes(models.Model):
    cod_docente = models.CharField(
        primary_key=True, max_length=10, null=False, blank=False)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=9999)


####clase asignarura###################################################################################################
class Asignaturas(models.Model):
    cod_asig = models.CharField(
        primary_key=True, max_length=10, null=False, blank=False)
    nom_asig = models.CharField(max_length=30)
    contenido_academico = models.CharField(max_length=500)
    Programa = models.ForeignKey(
        Programas, null=False, blank=False, on_delete=models.CASCADE)
    Docente = models.ForeignKey(
        Docentes, null=False, blank=False, on_delete=models.CASCADE)
    #Nivel_Asignatura = models.ForeignKey(Nivel_Asignatura,null=True,blank=True,on_delete = models.CASCADE)

    def _str_(self):

        return "({0}) {1}".format(self.cod_asig, self.nom_asig)


# class Detalle_Curso(models.Model):
 #   grupo = models.CharField(max_length=3)

  #  def _str_(self):
   #     return "{0}".format(self.grupo)
#clase Horario#######################################################################################################

#Clase curso##########################################################################################################
class Cursos(models.Model):
    cod_curso = models.CharField(max_length=10)
    nom_curso = models.CharField(max_length=30)
    grupo = models.CharField(max_length=3)
    dias = (('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'),
            ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'),)
    dia = models.CharField(max_length=10, choices=dias, default='',)
    horas_iniciales = (
        ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00',
                                                                 '11:00'), ('12:00', '12:00'), ('13:00', '13:00'),
        ('14:00', '14:00'), ('15:00', '15:00'), ('16:00',
                                                 '16:00'), ('17:00', '17:00'), ('18:00', '18:00'),
    )
    h_inicio = models.CharField(
        max_length=5, choices=horas_iniciales, default='8:00')
    horas_finales = (
        ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'),
        ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00',
                                                                     '17:00'), ('18:00', '18:00'), ('19:00', '19:00'),
        ('20:00', '20:00'),
    )
    h_final = models.CharField(
        max_length=5, choices=horas_finales, default='10:00')

    Programa = models.ForeignKey(
        Programas, null=False, blank=False, on_delete=models.CASCADE)

    # Detalle_Curso = models.ForeignKey(Detalle_Curso,null=False,blank=False,on_delete=models.CASCADE)

    def _str_(self):
        return "({0}) {1} [{2}]".format(self.cod_curso, self.nom_curso, self.dia, self.h_inicio)


#nivel asignatura###########################################################################################################
class Nivel_asignatura(models.Model):
    nivel = models.IntegerField(primary_key=True, null=False, blank=False)
    descripcion = models.CharField(max_length=200)
    Docente = models.ForeignKey(
        Docentes, null=False, blank=False, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(
        Asignaturas, null=False, blank=False, on_delete=models.CASCADE)


#nivel curso###########################################################################################################
class Nivel_Cursos(models.Model):
    nivel = models.IntegerField(primary_key=True, null=False, blank=False)
    descripcion = models.CharField(max_length=200)
    Curso = models.ForeignKey(
        Cursos, null=False, blank=False, on_delete=models.CASCADE)
    Docente = models.ForeignKey(
        Docentes, null=False, blank=False, on_delete=models.CASCADE)

    def _str_(self):
        return "({1})({2})".format(self.Curso, self.nivel)

#detalle curso#########################################################################################################


class detalle_curso(models.Model):
    grupo = models.IntegerField(primary_key=True, null=False)
    horario_inicial = models.DateField(
        (""), auto_now=False, auto_now_add=False)
    horario_final = models.DateField((""), auto_now=False, auto_now_add=False)
    estudiante = models.ForeignKey(
        Estudiantes,default="", null=False, blank=False, on_delete=models.CASCADE)
    Nivel_Curso = models.ForeignKey(
        Nivel_Cursos, null=False, blank=False, on_delete=models.CASCADE)


class usuario(models.Model):
    tipos_doc = (
        ('1', 'Cedula Ciudadania'), ('2', 'Tarjeta de identidad'), ('3',
                                                                    'Cedula de Extranjeria'), ('4', 'Certificado Cabildo '), ('5', 'Pasaporte'),
    )
    identificacion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=tipos_doc, default='2')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField(blank=False)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    correo = models.EmailField(blank=False)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(default="",max_length=60, blank=False)
    nom_programa = models.CharField(default="",max_length=60, blank=False)
    # hacer la relacion a user
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ciudad = models.ForeignKey(
        ciudad, default="", null=False, blank=False, on_delete=models.CASCADE)


#pagos###############################################################################################################
class Pagos(models.Model):
    id = models.CharField(primary_key=True, max_length=40,
                          null=False, blank=False)
    motivos = (
        ('1', 'Matricula'), ('2', 'Inscripcion'), ('3',
                                                   'Mensualidad'), ('4', 'Otros'),
    )
    motivo = models.CharField(max_length=1, choices=motivos, default='')
    Programa = models.ForeignKey(
        Programas, null=False, blank=False, on_delete=models.CASCADE)

#detalle_pago#########################################################################################################


class Detalle_Pagos(models.Model):
    class Meta:
        unique_together = (('Estudiante', 'Pagos'),)

    monto = models.IntegerField(null=False, blank=False)
    Fecha = models.DateTimeField(null=False)
    Estudiante = models.ForeignKey(
        Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    Pagos = models.ForeignKey(
        Pagos, null=False, blank=False, on_delete=models.CASCADE)
