from django.db import models
from curso.models import Curso

class Usuario(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(max_length=254)

class Inscripcion(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    id_usuario = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(to=Curso, on_delete=models.CASCADE)
