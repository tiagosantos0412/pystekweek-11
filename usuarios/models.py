from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField()
    cliente = models.CharField(max_length=4)
    