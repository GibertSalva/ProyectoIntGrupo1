from django.contrib import admin
from.models import *

# Register your models here.

class ImagenInline(admin.TabularInline):
    model = Imagen

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['precio',]
    inlines = [ImagenInline,]

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['user','propiedad','date',]


    

admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Ubicacion)
