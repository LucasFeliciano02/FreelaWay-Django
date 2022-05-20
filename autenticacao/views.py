from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User  # Essa classe é uma model que referencia o banco de dados
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


# Por padrão, o django vai procurar este arquivo cadastro.html dentro do seu app dentro de uma pasta criada por vc e chamada templates
# Criar dentro de templates o arquivo cadastro.html
def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/plataforma') 
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get("password")
        confirmar_senha = request.POST.get('confirm-password')
        
        # Validando informações e retornando para a pag inicial de cadastro
        if not senha == confirmar_senha: 
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')
        
        # .strip()  nao aceita espaço em branco
        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')
        
        # Filtra os usuarios do banco de dados, para nao poder criar um login com um nome ja existente, se existir ele redireciona pro login
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Esse usuário já existe')
            return redirect('/auth/cadastro')
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
        
            return redirect('/auth/logar')
        
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')
            

def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/plataforma')    
        return render(request, 'logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')  # Captura os dados que estao no logar.html
        senha = request.POST.get('password')
        
        # metodo autenticate do auth vai no banco de dados e verifica se ja existe algum usuario ou senha com essas credenciais
        usuario = auth.authenticate(username=username, password=senha)  
        
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/plataforma')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
        

# http://127.0.0.1:8000/auth/cadastro/

# http://127.0.0.1:8000/auth/logar/

# cadastro é a request de urlspatterns
# HttpResponse('Cadastro')  =  Ao acessar o navegador:   http://127.0.0.1:8000/auth/cadastro/, aparecera a msg ('Cadastro') que esta dentro do HttpResponse
