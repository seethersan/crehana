from django.db import models
from curso.models import Curso
from usuario.models import Usuario
from datetime import date

class ProgresoVideo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    minutos_rep_diaria = models.IntegerField()
    id_curso = models.ForeignKey(to=Curso, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    dia = models.DateField(default=date.today)
