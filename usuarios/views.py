from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Clientes
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
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
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    return render(request, 'cadastrar.html')


def home(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
    try:
        usuario = Usuarios.objects.get(id=usuario_id)
        cliente = Clientes.objects.get(cpf_cnpj=usuario.cpf)
        
        # Formatação da data_do_processo para dd/mm/yyyy
        data_do_processo = cliente.data_do_processo.split(" ")[0]  # Pega apenas a parte da data (yyyy-mm-dd)
        data_do_processo_formatada = data_do_processo[8:10] + '/' + data_do_processo[5:7] + '/' + data_do_processo[0:4]  # Formata para dd/mm/yyyy

        # Dados do cliente passados para o contexto
        context = {
            'nome': cliente.nome,
            'celular_1': cliente.celular_1,
            'valor': cliente.valor,
            'link': cliente.link,
            'tj': cliente.tj,
            'tipo': cliente.tipo,
            'processo': cliente.processo,
            'data_do_processo': data_do_processo_formatada,  # Data formatada
            'credor': cliente.credor,
        }
        return render(request, 'home.html', context)
    except Usuarios.DoesNotExist:
        return redirect('login')
    except Clientes.DoesNotExist:
        return render(request, 'home.html', {'error': 'Dados do cliente não encontrados'})


def logout(request):
    auth_logout(request)
    return redirect('login')

