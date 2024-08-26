from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.

def redirect_to_login(request):
    return redirect('login')

def login(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        try:
            usuario = Usuarios.objects.get(cpf=cpf)
            if check_password(senha, usuario.senha):
                # Armazena o ID do usuário na sessão
                request.session['usuario_id'] = usuario.id
                # Redireciona para a página de boas vindas
                return redirect('home')
            else:
                return HttpResponse('CPF ou senha incorretos!')
        except Usuarios.DoesNotExist:
            return HttpResponse('Usuário não encontrado!')
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
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    return render(request, 'cadastrar.html')


def home(request):
    # Recupera o id do início da sessão
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuarios.objects.get(id=usuario_id)
        # Retorna a página de boas-vindas com os dados do usuário
        return render(request, 'home.html', {
            'nome': usuario.nome,
            'cpf': usuario.cpf,
            'telefone': usuario.telefone
        })
    else:
        return redirect('login')

