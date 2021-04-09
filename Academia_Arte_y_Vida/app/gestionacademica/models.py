from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# periodo ############################################################################################################


class periodo(models.Model):
    codigo = models.IntegerField(primary_key=True , default="999")
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
    departamento = models.ForeignKey(departamento ,default="", null=False, blank=False, on_delete=models.CASCADE)

#clase Estudiante######################################################################################################


class Estudiantes(models.Model):
    tipos_doc = (
        ('1', 'Cedula Ciudadania'), ('2', 'Tarjeta de identidad'), ('3',
                                                                    'Cedula de Extranjeria'), ('4', 'Certificado Cabildo '), ('5', 'Pasaporte'),
    )
    identificacion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=60, choices=tipos_doc, default='2')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField(blank=False)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=60, choices=sexos, default='M')
    correo = models.EmailField(blank=False)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(default="",max_length=60, blank=False)
    curso_musica = models.CharField(default="",max_length=60, blank=True , null=True)
    # hacer la relacion a user
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ciudad = models.ForeignKey(
        ciudad, default="", null=True, blank=False, on_delete=models.CASCADE)
    


#clase programa########################################################################################################
class Programas(models.Model):
    cod_programa = models.CharField(primary_key=True, max_length=10)
    nom_programa = models.CharField(max_length=30)
    contenido_Aca = models.CharField(max_length=500)
    duracion = models.IntegerField(null=False,blank=False)

    def _str_(self):
        return "{0}".format(self.nom_programa)
    #     return "({0}) {1} Curso(s) = {2}, Asignatura(s) = {3}".format(self.cod_programa,self.nom_programa)

#clase inscripcion####################################################################################################

class inscripcionPrograma(models.Model):

    Id = models.IntegerField(primary_key=True,default=0,null=False,blank=False)

    # relaciones
    programa = models.ForeignKey(Programas,null=False,blank=False, on_delete= models.CASCADE)
    periodo = models.ForeignKey(periodo,null=False,blank=False, on_delete= models.CASCADE, default="999")
    

class InscripcionEstudiante(models.Model):

    Fecha_Realizacion = models.DateTimeField(auto_now_add=True)
    cod_inscripcionPrograma = models.ForeignKey(
        inscripcionPrograma, null=False, blank=False, on_delete=models.CASCADE )
    Estudiante = models.ForeignKey(
        Estudiantes, null=False, blank=False, on_delete=models.CASCADE , default="999")
    periodo = models.ForeignKey(
        periodo, default="999", null=False, blank=False, on_delete=models.CASCADE)

#Docentes ###############################################################################################################


class Docentes(models.Model):
    tipos_doc = (
        ('1', 'Cedula Ciudadania'), ('2', 'Tarjeta de identidad'), ('3',
                                                                    'Cedula de Extranjeria'), ('4', 'Certificado Cabildo '), ('5', 'Pasaporte'),
    )
    identificacion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=20, choices=tipos_doc, default='2')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField(blank=False)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=20, choices=sexos, default='M')
    correo = models.EmailField(blank=False)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(default="",max_length=60, blank=False)
    
    # hacer la relacion a user
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ciudad = models.ForeignKey(
        ciudad, default="", null=False, blank=False, on_delete=models.CASCADE)


####clase asignarura###################################################################################################
class Asignaturas(models.Model):
    cod_asig = models.CharField(
        primary_key=True, max_length=10, null=False, blank=False)
    nom_asig = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)

    def _str_(self):
        return "({0}) {1}".format(self.cod_asig, self.nom_asig)

#nivel asignatura###########################################################################################################
class Nivel_asignatura(models.Model):
    Id = models.IntegerField(primary_key=True)
    nivel = models.IntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=200)
    dia = models.CharField(max_length=100,null=True,blank=False)
    horaInicio = models.CharField(max_length=100,null=True , blank=True)
    horaFinal = models.CharField(max_length=100,null=True,blank=True)
    #relaciones
    cod_asignatura = models.ForeignKey(
        Asignaturas, null=False, blank=False, on_delete=models.CASCADE)
    docente = models.ForeignKey(
        Docentes, null=False, blank=False, on_delete=models.CASCADE)

class InscripcionAsignatura(models.Model):
    Id = models.IntegerField(primary_key=True,null=False, blank=False)

    # relaciones
    periodo = models.ForeignKey(periodo,null=False,blank=False ,on_delete=models.CASCADE)
    Id_inscripcionPrograma = models.ForeignKey(inscripcionPrograma, null=True, blank=True, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas,null=True,blank=True,on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel_asignatura, null=False, blank=False, on_delete=models.CASCADE)


    


class InscripcionEstudianteAsignatura(models.Model):

    fecha_realizacion = models.DateField(default="",null=False,blank=False)
    nivel_asignatura = models.ForeignKey(Nivel_asignatura, null=False, blank=False, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    inscripcion_estudiante = models.ForeignKey(InscripcionEstudiante,default="", null=True, blank=True, on_delete=models.CASCADE)

#Clase curso##########################################################################################################
class Cursos(models.Model):
    cod_curso = models.CharField(primary_key=True, null=False, blank=False,max_length=10)
    nom_curso = models.CharField(max_length=30)

    def _str_(self):
        return "({0}) {1} [{2}]".format(self.cod_curso, self.nom_curso, self.dia, self.h_inicio)

#nivel curso###########################################################################################################


class InscripcionCurso(models.Model):
    Id = models.IntegerField(primary_key=True,null=False, blank=False)

    # relaciones
    Id_inscripcionPrograma = models.ForeignKey(inscripcionPrograma, null=True, blank=True, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, null=False, blank=False, on_delete=models.CASCADE)
    periodo = models.ForeignKey(periodo, null=False, blank=False, on_delete=models.CASCADE)

class Nivel_Cursos(models.Model):
    Id = models.IntegerField(primary_key=True)
    nivel = models.IntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=200)

    #relaciones

    inscripcion_curso = models.ForeignKey(InscripcionCurso,default="999", null=False, blank=False, on_delete=models.CASCADE)
    periodo = models.ForeignKey(periodo,default="999", null=False, blank=False, on_delete=models.CASCADE)
    def _str_(self):
        return "({1})({2})".format(self.Curso, self.nivel)

#detalle curso#########################################################################################################


class detalle_curso(models.Model):
    grupo = models.IntegerField(null=False , blank=False)
    
    dia = models.CharField(max_length=100,null=True,blank=False)
    horaInicio = models.CharField(max_length=100,null=True , blank=True)
    horaFinal = models.CharField(max_length=100,null=True,blank=True)

    #relaciones
    Docente = models.ForeignKey(
        Docentes, null=False, blank=False, on_delete=models.CASCADE)
    periodo = models.ForeignKey(periodo,default="", null=False, blank=False, on_delete=models.CASCADE)
    Nivel_Curso = models.ForeignKey(Nivel_Cursos,default="", null=False, blank=False, on_delete=models.CASCADE)
    InscripcionCurso = models.ForeignKey(InscripcionCurso,default="999", null=True, blank=True, on_delete=models.CASCADE)
    inscripcion_programa = models.ForeignKey(inscripcionPrograma,default="999", null=True, blank=True, on_delete=models.CASCADE)

# inscripcion del estudiante en el detalle_curso

class inscripcionEstudianteCurso(models.Model):
    
    detalle_curso = models.ForeignKey(detalle_curso,default="9999", null=False, blank=False, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiantes,default="9999", null=False, blank=False, on_delete=models.CASCADE)

    inscripcion_programa_estudiante = models.ForeignKey(InscripcionEstudiante,default="", null=True, blank=True, on_delete=models.CASCADE)
    

class usuario(models.Model):
    tipos_doc = (
        ('1', 'Cedula Ciudadania'), ('2', 'Tarjeta de identidad'), ('3',
                                                                    'Cedula de Extranjeria'), ('4', 'Certificado Cabildo '), ('5', 'Pasaporte'),
    )
    identificacion = models.IntegerField(primary_key=True)
    pagoRealizado = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20, choices=tipos_doc, default='2')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField(blank=False)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=20, choices=sexos, default='M')
    correo = models.EmailField(blank=False)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(default="",max_length=60, blank=False)
    curso_musica = models.CharField(default="",max_length=60, blank=True , null=True)
    nom_programa = models.CharField(default="",max_length=60, blank=False)
    referenciaPago = models.IntegerField(null=True,blank=True)
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

#detalle_pago#########################################################################################################


class Detalle_Pagos(models.Model):
    monto = models.IntegerField(null=False, blank=False)
    Fecha = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    cod_Estudiante = models.ForeignKey(
        Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    id_Pago = models.ForeignKey(
        Pagos, null=False, blank=False, on_delete=models.CASCADE)

class actividades(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    # archivo

    file = models.FileField(upload_to="actividades/", null=True, blank=True)

    #relaciones
    Detalle_curso = models.ForeignKey(
        detalle_curso, null=True, blank=True, on_delete=models.CASCADE)
    Nivel_asignatura = models.ForeignKey(
        Nivel_asignatura, null=True, blank=True, on_delete=models.CASCADE)


class pqrs(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    email = models.EmailField(blank=False)
    solicitante = (('1', 'Estudiante'), ('2', 'Colaborador'), ('3', 'Docente'), 
                ('4','Egresado'), ('5', 'Externo'), ('6', 'Proveedor'), ('7', 'Otro'))
    tipoSolicitante = models.CharField(max_length=20, choices=solicitante, default='')
    celular = models.CharField(max_length=10)
    solicitud = (('1', 'Felicitaciones'), ('2', 'Sugerencias'), ('3', 'Peticiones'), 
                ('4','Quejas'), ('5', 'Reclamos'), ('6', 'Comentarios'), ('7', 'Otro'))
    tipoSolicitud = models.CharField(max_length=20, choices=solicitud, default='')
    servicio = (('1', 'Académicos'), ('2', 'Administrativos'), ('3', 'Consultor'), 
                ('4','Tecnología'), ('5', 'Otro'))
    solicitudServicio = models.CharField(max_length=20, choices=servicio, default='')
    comentario = models.TextField(max_length=1000)

    # Relaciones
    ciudad = models.ForeignKey(
        ciudad, default="", null=False, blank=False, on_delete=models.CASCADE)


class contacto(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(blank=False)
    mensaje = models.TextField(max_length=1000)