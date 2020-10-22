from django.contrib import admin
from.models import *

# Register your models here.

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['usuario','titulo',]

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['usuario','propiedad','mensaje']

admin.site.register(Contacto)
admin.site.register(Usuario)
admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Consulta,ConsultaAdmin)
