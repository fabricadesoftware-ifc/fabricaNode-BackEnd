from django.db import models

from .estado import estado


class cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(estado, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.nome}({self.estado.sigla})'
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']