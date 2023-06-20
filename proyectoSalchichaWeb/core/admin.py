from django.contrib import admin
from .models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut_cliente', 'nombre_cliente', 'email', 'telefono', 'direccion']
    search_fields = ['rut_cliente', 'nombre_cliente']
    list_per_page = 15

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen']
    search_fields = ['nombre_producto']
    list_per_page = 15


class BoletaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'metodo_pago', 'total' ]
    list_filter = ['metodo_pago', 'cliente']
    list_per_page = 15

class DetalleBoletaAdmin(admin.ModelAdmin):
    list_display = ['id', 'producto', 'boleta', 'cantidad', 'precio_unitario']
    list_filter = ['producto', 'boleta']
    list_per_page = 15


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Boleta, BoletaAdmin)
admin.site.register(DetalleBoleta, DetalleBoletaAdmin)