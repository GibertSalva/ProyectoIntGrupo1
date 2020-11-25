from django.contrib import admin
from.models import *

# Register your models here.

class ImagenInline(admin.TabularInline):
    model = Imagen

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['titulo','usuario','precio','ubicacion','tipo','estado']
    list_filter = ['ubicacion','tipo','estado']
    search_fields = ['usuario__username','titulo']
    inlines = [ImagenInline,]
    fieldsets = (
        ("Datos de la Propiedad", {
            'fields': ('usuario', 'titulo','precio','tipo','estado','habitaciones','baños','tamaño','descripcion')
        }),
        ('Ubicacion', {
            'fields': ('ubicacion','barrio','calle','numero')
        }),
    )

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['user','propiedad','date',]
    list_filter = ['user','propiedad']
    search_fields = ['user__username','propiedad__titulo']

class ImagenAdmin(admin.ModelAdmin):
    list_display = ['foto','propiedad']
    list_filter = ['propiedad']
    search_fields = ['propiedad__titulo']

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['provincia']
    search_fields = ['provincia']



    

admin.site.register(Propiedad,PropiedadAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Imagen,ImagenAdmin)
