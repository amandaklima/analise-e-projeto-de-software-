from django.db import models

class Usuario(models.Model):
    TIPOS = [
        ('funcional', 'Analfabetismo Funcional'),
        ('absoluto', 'Analfabetismo Absoluto'),
    ]
    
    niveis = [
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    tipo_analfabetismo = models.CharField(max_length=20, choices=TIPOS)
    nivel = models.CharField(max_length=20, choices=niveis)

    def __str__(self):
        return self.nome
