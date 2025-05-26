from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensagem
from usuarios.models import Usuario

def mensagens_lista(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    mensagens = Mensagem.objects.filter(destinatario=usuario).order_by('-enviado_em')
    return render(request, 'mensagens/lista.html', {'mensagens': mensagens})

def enviar_mensagem(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        destinatario_id = request.POST.get('destinatario_id')
        conteudo = request.POST.get('conteudo')
        destinatario = get_object_or_404(Usuario, id=destinatario_id)
        Mensagem.objects.create(remetente=usuario, destinatario=destinatario, conteudo=conteudo)
        return redirect('mensagens_lista')
    usuarios = Usuario.objects.exclude(id=usuario.id)
    return render(request, 'mensagens/enviar.html', {'usuarios': usuarios})
