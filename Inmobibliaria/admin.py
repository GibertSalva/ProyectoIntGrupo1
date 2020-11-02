from django.contrib import admin
from.models import *

# Register your models here.

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['precio',]

class ConsultaAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['usuario','propiedad','mensaje']
    
=======
    list_display = ['propiedad','mensaje']

>>>>>>> eb8c369ecdb8df24dd56d24664c7fdabc0eb9ff9

admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Ubicacion)