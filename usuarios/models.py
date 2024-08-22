from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    senha = models.CharField(max_length=200)
    cliente = models.CharField(max_length=4)
    