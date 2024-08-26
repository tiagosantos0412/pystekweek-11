from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=250)
    cliente = models.CharField(max_length=4)
    