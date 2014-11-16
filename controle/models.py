from django.db import models


class Controle(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=3) 
    nrodoc = models.CharField(max_length=15)
    Ativo = 'A'
    Inativo = 'I'
    sta = ((Ativo,'Ativo'), (Inativo, 'Inativo'))
    
    status = models.CharField(max_length='2', choices=sta, default='Ativo')
    