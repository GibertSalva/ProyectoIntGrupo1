from django.contrib import admin
from.models import *

# Register your models here.

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['precio',]

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['propiedad','mensaje']


admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Ubicacion)