from django.db import models

# Create your models here.
class Contacto(models.Model):
    telefono = models.CharField(max_length=20)
    mail = models.EmailField()
    