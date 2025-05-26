from django.shortcuts import render, redirect, get_object_or_404
from .models import Atividade, Resposta
from usuarios.models import Usuario

def lista_atividades(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    atividades = Atividade.objects.filter(tipo=usuario.tipo_analfabetismo, nivel=usuario.nivel)
    return render(request, 'atividades/lista.html', {'atividades': atividades})

def criar_atividade(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tipo = request.POST.get('tipo')
        nivel = request.POST.get('nivel')
        Atividade.objects.create(titulo=titulo, tipo=tipo, nivel=nivel, criador=usuario)
        return redirect('lista_atividades')
    return render(request, 'atividades/criar.html')

def responder_atividade(request, atividade_id):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    atividade = get_object_or_404(Atividade, id=atividade_id)
    if request.method == 'POST':
        resposta_texto = request.POST.get('resposta', '')
        acerto = "correto" in resposta_texto.lower()
        Resposta.objects.create(usuario=usuario, atividade=atividade, resposta_texto=resposta_texto, acerto=acerto)
        return redirect('feedback_atividade', atividade_id=atividade.id)
    return render(request, 'atividades/responder.html', {'atividade': atividade})

def feedback_atividade(request, atividade_id):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    resposta = Resposta.objects.filter(usuario=usuario, atividade_id=atividade_id).last()
    if not resposta:
        return redirect('lista_atividades')
    return render(request, 'atividades/feedback.html', {'resposta': resposta})
