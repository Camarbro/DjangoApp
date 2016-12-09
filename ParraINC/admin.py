from django.contrib import admin
from .models import Inventario, Area, Empleado_Produccion, Pedido, Empleado_Jefe, Empleado_Almacen, Empleado_Calidad

# Register your models here.

@admin.register(Inventario)
class Inventario_admin(admin.ModelAdmin):
    list_display = ('codigo_pieza', 'nombre_pieza','precio_unitario','stock')

@admin.register(Area)
class Area_admin(admin.ModelAdmin):
    list_display = ('codigo_area', 'nombre_area')

@admin.register(Empleado_Jefe)
class Jefe_admin(admin.ModelAdmin):
    list_display =('usuario', 'area_empleado', 'nombre_empleado' , 'puesto_empleado')

@admin.register(Empleado_Produccion)
class Produccion_admin(admin.ModelAdmin):
    list_display =('usuario', 'area_empleado', 'nombre_empleado' , 'puesto_empleado')

@admin.register(Empleado_Calidad)
class Calidad_admin(admin.ModelAdmin):
    list_display =('usuario', 'area_empleado', 'nombre_empleado' , 'puesto_empleado')

@admin.register(Empleado_Almacen)
class Almacen_admin(admin.ModelAdmin):
    list_display =('usuario', 'area_empleado', 'nombre_empleado' , 'puesto_empleado')

@admin.register(Pedido)
class Pedido_admin(admin.ModelAdmin):
    list_display = ('numero_pedido','entrega','recibe', 'jefe_linea','fecha_entrega','get_piezas','terminado')
