from django.db import models

from .publicacao import publicacao
from .keyword import keyword


class publicacao_keyword(models.Model):
    publicacao = models.ForeignKey(publicacao, on_delete=models.RESTRICT)
    keyword = models.ForeignKey(keyword, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.publicacao.titulo} - {self.keyword.palavra}'
    
    class Meta:
        verbose_name = 'Publicação Keyword'
        verbose_name_plural = 'Publicações Keywords'
        ordering = ['publicacao']