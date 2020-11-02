from django.db import models
from django.contrib.auth.models import User



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
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    def __str__(self):
        return "{} {}".format(self.calle,self.numero)

class Propiedad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length=20)
    precio = models.IntegerField()
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, null=False)
    tipo = models.CharField(max_length=12,choices=TIPO_CHOICES,default='Casa')
    estado = models.CharField(max_length=8,choices=STATUS_CHOICES,default='Venta')
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    tamaño = models.IntegerField()
    imagenes = models.ImageField(max_length=100, upload_to='fotos/', blank=True)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return "{}".format(self.titulo)


class Consulta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    propiedad = models.ForeignKey('Propiedad', on_delete=models.CASCADE, null=False)
    mensaje = models.CharField(max_length=200)
    def __str__(self):
        return "{}".format(self.usuario)

