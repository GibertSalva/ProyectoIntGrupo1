from django.contrib import admin
from.models import *

# Register your models here.

class ImagenInline(admin.TabularInline):
    model = Imagen

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['precio',]
    inlines = [ImagenInline,]


    

admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Comentario)
admin.site.register(Ubicacion)
