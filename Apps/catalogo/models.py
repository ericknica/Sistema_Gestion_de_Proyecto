# apps/catalogos/models.py
from django.db import models
from Apps.seguridad.usuarios.models import Usuario  
from Apps.catalogo.municipio.models import Municipio
from Apps.catalogo.tipoEntrada.models import TipoEntrada
from Apps.catalogo.tipoSalida.models import TipoSalida # Para asignar un responsable

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    tipos_entrada = models.ManyToManyField(TipoEntrada)
    tipos_salida = models.ManyToManyField(TipoSalida)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    

class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name="tareas", on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Finalizada', 'Finalizada')])

    def __str__(self):
        return self.descripcion
