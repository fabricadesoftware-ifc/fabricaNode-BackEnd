from django.db import models

from .cidade import Cidade

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']
