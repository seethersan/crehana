from django.db import models
from curso.models import Curso, Categoria
from usuario.models import Usuario, Inscripcion
from datetime import date

class ProgresoVideo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    minutos_rep_diaria = models.IntegerField()
    curso = models.ForeignKey(to=Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE)
    inscripcion = models.ForeignKey(to=Inscripcion, on_delete=models.CASCADE)
    dia = models.DateField(default=date.today)
