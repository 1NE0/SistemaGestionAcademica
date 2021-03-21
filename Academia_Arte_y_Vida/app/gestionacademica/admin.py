from django.contrib import admin
from Academia_Arte_y_Vida.app.gestionacademica.models import *

# Register your models here.

admin.site.register(Docentes)
admin.site.register(Programas)
admin.site.register(Asignaturas)
admin.site.register(Cursos)
admin.site.register(Nivel_Cursos)
admin.site.register(Estudiantes)
admin.site.register(detalle_curso)
admin.site.register(InscripcionEstudiante)
admin.site.register(inscripcionPrograma)
admin.site.register(InscripcionAsignatura)
admin.site.register(InscripcionCurso)
admin.site.register(actividades)
admin.site.register(Pagos)
admin.site.register(Detalle_Pagos)
admin.site.register(usuario)
admin.site.register(periodo)
admin.site.register(ciudad)
admin.site.register(departamento)



