from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_profesor = models.BooleanField(default=False)
    is_estudiante = models.BooleanField(default=False)

class Profesor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Estudiante(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=100)
    estudiante = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    nombre_profesor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    patrocinado = models.BooleanField(default=False)  
    profesor_patrocinador = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_patrocinados')  # Profesor que patrocina el proyecto

    def __str__(self):
        return self.nombre_proyecto
