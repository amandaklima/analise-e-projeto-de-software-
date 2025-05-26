from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(senha, usuario.senha):
                request.session['usuario_id'] = usuario.id
                return redirect('perfil')
            else:
                messages.error(request, "Senha incorreta.")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
    return render(request, 'usuarios/login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = make_password(request.POST['senha'])
        tipo = request.POST['tipo']
        nivel = request.POST['nivel']
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado.")
            return redirect('cadastro')
        usuario = Usuario(nome=nome, email=email, senha=senha, tipo_analfabetismo=tipo, nivel=nivel)
        usuario.save()
        messages.success(request, "Cadastro realizado! Faça login.")
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def perfil(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuarios/perfil.html', {'usuario': usuario})
