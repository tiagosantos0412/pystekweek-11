from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=250)
    cliente = models.CharField(max_length=4)
    
class Clientes(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, default=1)
    data_do_arquivo = models.CharField(max_length=20)
    nome = models.CharField(max_length=250)
    celular_1 = models.CharField(max_length=20)
    valor = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    tj = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    processo = models.CharField(max_length=50)
    celular_2 = models.CharField(max_length=20)
    cpf_cnpj= models.CharField(max_length=50)
    data_do_processo = models.CharField(max_length=20)
    credor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.processo
