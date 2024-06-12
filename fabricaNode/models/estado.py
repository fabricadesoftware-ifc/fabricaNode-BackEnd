from django.db import models

from .pais import Pais

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.sigla}-{self.nome}'
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['sigla']