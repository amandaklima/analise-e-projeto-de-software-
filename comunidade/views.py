from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from usuarios.models import Usuario

def comunidade_lista(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'comunidade/lista.html', {'posts': posts})

def criar_post(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        Post.objects.create(autor=usuario, titulo=titulo, conteudo=conteudo)
        return redirect('comunidade_lista')
    return render(request, 'comunidade/criar.html')
