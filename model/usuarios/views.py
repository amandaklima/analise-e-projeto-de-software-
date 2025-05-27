from django.shortcuts import render, redirect
from .models import Usuario

def cadastro(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        tipo = request.POST['tipo']
        nivel = request.POST['nivel']
        Usuario.objects.create(
            nome=nome, email=email, senha=senha,
            tipo_analfabetismo=tipo, nivel=nivel
        )
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            request.session['usuario_id'] = usuario.id
            return redirect('perfil')
        except Usuario.DoesNotExist:
            return render(request, 'usuarios/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'usuarios/login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def perfil(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'usuarios/perfil.html', {'usuario': usuario})
