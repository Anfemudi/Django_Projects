from django.contrib import admin
from gestionpedidos.models import Clientes,Articulos,Pedios


class ClientesAdmin(admin.ModelAdmin):

    ## Muestra como se vera el elemento en la consola admin
    list_display=("nombre","direccion","telefono")
    #campo de busqueda por las columnas especificadas
    search_fields=("nombre","telefono")


class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"   
     


admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedios,PedidosAdmin)

# Register your models here.

