from django.db import models

from .publicacao import Publicacao
from .keyword import Keyword


class Publicacao_keyword(models.Model):
    publicacao = models.ForeignKey(Publicacao, on_delete=models.RESTRICT)
    keyword = models.ForeignKey(Keyword, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.publicacao.titulo} - {self.keyword.palavra}'
    
    class Meta:
        verbose_name = 'Publicação Keyword'
        verbose_name_plural = 'Publicações Keywords'
        ordering = ['publicacao']