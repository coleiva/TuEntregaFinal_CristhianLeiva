from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class JuegoNvo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()
    imagen = models.ImageField(upload_to='juegos_img/', null=True, blank=True)
    consola = models.CharField(max_length=20, default='Juego PC')

    def __str__(self):
        return self.nombre

class UsuarioLogin(AbstractUser):
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)

    def __str__(self):
        return self.username