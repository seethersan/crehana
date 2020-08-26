from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Categoria(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100, validators=[MinLengthValidator(3, "Invalid category name"), MaxLengthValidator(55, "Invalid category name")])

class Curso(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(3, "Invalid category name"), MaxLengthValidator(55, "Invalid category name")])
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE)
