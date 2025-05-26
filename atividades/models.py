from django.db import models
from usuarios.models import Usuario

class Atividade(models.Model):
    TIPOS = [('funcional', 'Funcional'), ('absoluto', 'Absoluto')]
    NIVEIS = [('iniciante', 'Iniciante'), ('intermediario', 'Intermediário'), ('avancado', 'Avançado')]

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    nivel = models.CharField(max_length=20, choices=NIVEIS)
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Resposta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    resposta_texto = models.TextField()
    acerto = models.BooleanField()

    def __str__(self):
        return f"{self.usuario.nome} - {self.atividade.titulo}"
