from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from django.contrib.auth.hashers import make_password
# Create your views here.

def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = make_password(request.POST.get('senha'))  # Criptografa a senha
        cliente = request.POST.get('cliente')

        # Criação do usuário
        usuario = Usuarios(nome=nome, cpf=cpf, telefone=telefone, email=email, senha=senha, cliente=cliente)
        usuario.save()

        return HttpResponse('Usuário cadastrado com sucesso')
    return render(request, 'cadastrar.html')

