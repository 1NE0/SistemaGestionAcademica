from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#clase programa########################################################################################################
class Programas(models.Model):
    cod_programa = models.CharField(primary_key=True,max_length=10)
    nom_programa = models.CharField(max_length=30)
    contenido_Aca = models.CharField(max_length=500)
    #Curso = models.ForeignKey(Cursos,null=True,blank=True,on_delete=models.CASCADE)
    #Asignatura = models.ForeignKey(Asignaturas,null=True,blank=True,on_delete=models.CASCADE)
    # FALTA 

    def _str_(self):
        return "{0}".format(self.nom_programa)
    #     return "({0}) {1} Curso(s) = {2}, Asignatura(s) = {3}".format(self.cod_programa,self.nom_programa)

#Docentes ###############################################################################################################
class Docentes(models.Model):
    cod_docente = models.CharField(primary_key=True, max_length=10, null=False,blank=False)
    nombres = models.CharField(max_length= 25)
    apellidos = models.CharField(max_length= 25)
    user = models.OneToOneField(User, on_delete=models.CASCADE ,default=9999)


####clase asignarura###################################################################################################
class Asignaturas(models.Model):
    cod_asig = models.CharField(primary_key=True, max_length=10, null=False,blank=False)
    nom_asig = models.CharField(max_length=30)
    contenido_academico = models.CharField(max_length=500)
    nivel = models.IntegerField(null=False, blank=False)
    Programa = models.ForeignKey(Programas,null=False,blank=False,on_delete=models.CASCADE)
    Docente = models.ForeignKey(Docentes, null = False, blank= False, on_delete= models.CASCADE)
    #Nivel_Asignatura = models.ForeignKey(Nivel_Asignatura,null=True,blank=True,on_delete = models.CASCADE)

    def _str_(self):
        
        return "({0}) {1}".format(self.cod_asig,self.nom_asig)



#class Detalle_Curso(models.Model):
 #   grupo = models.CharField(max_length=3)

  #  def _str_(self):
   #     return "{0}".format(self.grupo)
#clase Horario#######################################################################################################
"""
class Horarios(models.Model):

    dias = (('1','Lunes'),('2','Martes'),('3','Miercoles'),('4','Jueves'),('5','Viernes'),('6','Sabado'),)
    dia = models.CharField(max_length=1,choices=dias,default='')
    horas_iniciales = (
        ('1','8:00'), ('2','9:00'),('3','10:00'),('4','11:00'),('5','12:00'),('6','13:00'),
        ('7','14:00'),('8','15:00'),('9','16:00'),('10','17:00'),('11','18:00'),
    )
    h_inicio = models.CharField(max_length=5,choices=horas_iniciales,default='1')
    horas_finales = (
        ('1','10:00'),('2','11:00'),('3','12:00'),('4','13:00'),
        ('5','14:00'),('6','15:00'),('7','16:00'),('8','17:00'),('9','18:00'),
    )
    h_final = models.CharField(max_length=1,choices=horas_finales,default='1')

    def _str_(self):
        return "({0})".format(self.dia,self.h_inicio,self.h_final)

"""
#Clase curso##########################################################################################################
class Cursos(models.Model):
    cod_curso = models.CharField(max_length=10)
    nom_curso = models.CharField(max_length=30)
    grupo = models.CharField(max_length=3)
    dias = (('1','Lunes'),('2','Martes'),('3','Miercoles'),('4','Jueves'),('5','Viernes'),('6','Sabado'),)
    dia = models.CharField(max_length=1,choices=dias,default='')
    horas_iniciales = (
        ('1','8:00'), ('2','9:00'),('3','10:00'),('4','11:00'),('5','12:00'),('6','13:00'),
        ('7','14:00'),('8','15:00'),('9','16:00'),('10','17:00'),('11','18:00'),
    )
    h_inicio = models.CharField(max_length=5,choices=horas_iniciales,default='1')
    horas_finales = (
        ('1','10:00'),('2','11:00'),('3','12:00'),('4','13:00'),
        ('5','14:00'),('6','15:00'),('7','16:00'),('8','17:00'),('9','18:00'),
    )
    h_final = models.CharField(max_length=1,choices=horas_finales,default='1')
    #Nivel_Curso= models.ForeignKey(Nivel_Curso,null=False,blank=False,on_delete=models.CASCADE)
    Programa = models.ForeignKey(Programas,null=False,blank=False,on_delete=models.CASCADE)


    # Detalle_Curso = models.ForeignKey(Detalle_Curso,null=False,blank=False,on_delete=models.CASCADE)

    def _str_(self):
        return "({0}) {1} [{2}]".format(self.cod_curso,self.nom_curso,self.dia,self.h_inicio)


#nivel curso###########################################################################################################
class Nivel_Cursos(models.Model):
    nivel = models.IntegerField(primary_key=True, null=False,blank=False)
    Curso = models.ForeignKey(Cursos, null=False,blank=False,on_delete=models.CASCADE)
    Docente = models.ForeignKey(Docentes, null = False, blank= False, on_delete= models.CASCADE)
    def _str_(self):
        return "({1})({2})".format(self.Curso,self.nivel)

#clase Estudiante######################################################################################################
class Estudiantes(models.Model):
    identificacion = models.IntegerField(primary_key=True)
    tipos_doc = (
        ('1','Cedula Ciudadania'),('2','Tarjeta de identidad'),('3','Cedula de Extranjeria'),('4','Certificado Cabildo '),('5','Pasaporte'),
    )
    tipo=models.CharField(max_length=1, choices=tipos_doc, default='2')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length = 30)
    edad = models.IntegerField(blank=False)
    sexos=(('F','Femenino'),('M','Masculino'))
    sexo =models.CharField(max_length = 1, choices=sexos, default='M')
    correo = models.EmailField(blank = False)
    telefono = models.CharField(max_length=12)

    # hacer la relacion a user
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


#clase inscripcion####################################################################################################
class Inscripciones(models.Model):
    class Meta:
        unique_together = (('Programa', 'Estudiante'),)

    Fecha_Realizacion = models.DateTimeField(auto_now_add=True)
    Programa = models.ForeignKey(Programas,null=False,blank=False,on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(Estudiantes, null=False,blank=False,on_delete=models.CASCADE)


#pagos###############################################################################################################
class Pagos(models.Model):
    id = models.CharField(primary_key=True, max_length= 40, null=False, blank=False)
    motivos = (
        ('1', 'Matricula'),('2','Inscripcion'),('3','Mensualidad'),('4','Otros'),
    )
    motivo = models.CharField(max_length=1, choices=motivos, default='')
    Programa = models.ForeignKey(Programas,null=False,blank = False,on_delete = models.CASCADE)

#detalle_pago#########################################################################################################
class Detalle_Pagos(models.Model):
    class Meta:
        unique_together = (('Estudiante', 'Pagos'),)

    monto = models.IntegerField(null=False, blank=False)
    Fecha = models.DateTimeField(null= False)
    Estudiante = models.ForeignKey(Estudiantes, null=False,blank=False, on_delete=models.CASCADE)
    Pagos =models.ForeignKey(Pagos,null=False,blank=False, on_delete=models.CASCADE)
