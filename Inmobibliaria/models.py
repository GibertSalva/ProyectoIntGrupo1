from django.db import models

# Create your models here.
class Contacto(models.Model):
    telefono = models.CharField(max_length=20)
    mail = models.EmailField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return "{}".format(self.nombre)


class Propiedad(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    habitaciones = models.IntegerField(max_length=20)
    dormitorios = models.IntegerField(max_length=20)
    baños = models.IntegerField(max_length=20)
    imagenes = models.ImageField(max_length=100, upload_to='fotos/', blank=True)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return "{}".format(self.titulo)


class Consulta(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
    propiedad = models.ForeignKey('Propiedad', on_delete=models.CASCADE, null=False)
    mensaje = models.CharField(max_length=200)

