from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.utils.timezone import now



STATUS_CHOICES = [
        ('Alquiler', 'En Alquiler'),
        ('Venta', 'En Venta'),
    ]

TIPO_CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Garaje', 'Garaje'),
        ('Oficina', 'Oficina'),
    ]

class Ubicacion(models.Model):
    provincia = models.CharField(max_length=30)
    def __str__(self):
        return "{}".format(self.provincia)


class Propiedad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length=20)
    precio = models.IntegerField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, null=False)
    barrio = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    tipo = models.CharField(max_length=12,choices=TIPO_CHOICES)
    estado = models.CharField(max_length=8,choices=STATUS_CHOICES,default='Venta')
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    tamaño = models.IntegerField()
    descripcion = models.TextField(max_length=2000)
    auto_now = timezone.now()
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}".format(self.titulo)

class Imagen(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE,null=False)
    foto = models.ImageField(upload_to='fotos/', null=True)


class Comentario(models.Model): 
    propiedad = models.ForeignKey(Propiedad, related_name="comments", on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s - %s" % (self.propiedad.titulo, self.user)




