from django.contrib import admin
from.models import *

# Register your models here.

class ImagenInline(admin.TabularInline):
    model = Imagen

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['precio',]
    inlines = [ImagenInline,]

class ConsultaAdmin(admin.ModelAdmin):

    list_display = ['usuario','propiedad','mensaje']
    

admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Ubicacion)