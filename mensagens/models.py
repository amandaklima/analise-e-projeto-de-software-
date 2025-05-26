from django.db import models
from usuarios.models import Usuario

class Mensagem(models.Model):
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    conteudo = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.remetente.nome} para {self.destinatario.nome}"
