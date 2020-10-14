from django.db import models

# Create your models here.
class Contacto(models.Model):
    telefono = models.CharField(max_length=20)
    mail = models.EmailField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    contacto = models.ForeingKey('Contacto', on_delete=models.CASACADE, null=False)

class Propiedad(models.Model):
    titulo = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    habitaciones = models.IntegerField()
    dormitorios = models.IntegerField()
    baños = models.IntegerField()
    imagenes = models.ImageField(max_length=100, upload_to='fotos/', blank=True)
    descripcion = models.CharField()

class Consulta(models.Model):
    usuario = models.ForeingKey('Usuario', on_delete=models.CASACADE, null=False)
    propiedad = models.ForeingKey('Propiedad', on_delete=models.CASACADE, null=False)
    mensaje = models.CharField()
 