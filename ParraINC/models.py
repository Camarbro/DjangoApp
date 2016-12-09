from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Area(models.Model):
    codigo_area = models.IntegerField()
    nombre_area = models.CharField(max_length = 64)

    def __unicode__(self):
        return (self.nombre_area)

class Inventario(models.Model):
    codigo_pieza =  models.IntegerField()
    nombre_pieza = models.CharField(max_length = 64)
    area_pieza = models.ForeignKey(Area)
    precio_unitario = models.FloatField()
    stock = models.IntegerField()

    def __unicode__(self):
        return (self.nombre_pieza)

class Empleado_Produccion(models.Model):
    usuario = models.OneToOneField(User)
    area_empleado = models.ForeignKey(Area)
    nombre_empleado = models.CharField(max_length = 64)
    PUESTOS = (
        ('Produccion', 'PRODUCCION'),
        ('Otro', 'Otro')
    )
    puesto_empleado = models.CharField(max_length = 10, choices = PUESTOS, default = 'Produccion')

    def __unicode__(self):
        return (self.nombre_empleado)

class Empleado_Jefe(models.Model):
    usuario = models.OneToOneField(User)
    area_empleado = models.ForeignKey(Area)
    nombre_empleado = models.CharField(max_length = 64)
    PUESTOS = (
        ('Jefe_Linea', 'JEFE LINEA'),
        ('Otro', 'Otro')
    )
    puesto_empleado = models.CharField(max_length = 10, choices = PUESTOS, default = 'Produccion')
    pedidos_activos = models.IntegerField()

    def __unicode__(self):
        return (self.nombre_empleado)

class Empleado_Almacen(models.Model):
    usuario = models.OneToOneField(User)
    area_empleado = models.ForeignKey(Area)
    nombre_empleado = models.CharField(max_length = 64)
    PUESTOS = (
        ('Almacen', 'ALMACEN'),
        ('Otro', 'Otro')
    )
    puesto_empleado = models.CharField(max_length = 10, choices = PUESTOS, default = 'Produccion')

    def __unicode__(self):
        return (self.nombre_empleado)

class Empleado_Calidad(models.Model):
    usuario = models.OneToOneField(User)
    area_empleado = models.ForeignKey(Area)
    nombre_empleado = models.CharField(max_length = 64)
    PUESTOS = (
        ('Calidad', 'CALIDAD'),
        ('Otro', 'Otro')
    )
    puesto_empleado = models.CharField(max_length = 10, choices = PUESTOS, default = 'Produccion')


    def __unicode__(self):
        return (self.nombre_empleado)

class Pedido(models.Model):
    numero_pedido = models.IntegerField()
    area = models.ForeignKey(Area)
    entrega = models.ForeignKey(Empleado_Almacen, null = True)
    recibe = models.ForeignKey(Empleado_Produccion, null = True)
    jefe_linea = models.ForeignKey(Empleado_Jefe, null = True )
    fecha_entrega = models.DateTimeField (default = timezone.now)
    piezas = models.ManyToManyField(Inventario)
    control_calidad = models.BooleanField(default = False)
    terminado = models.BooleanField(default = False)

    def get_piezas(self):
        return "\n".join([p.nombre_pieza for p in self.piezas.all()])
