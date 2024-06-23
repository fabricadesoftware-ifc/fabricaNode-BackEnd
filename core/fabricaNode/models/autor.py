from django.db import models

from .cidade import Cidade
from .subarea import Subarea


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    dataNascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.RESTRICT)
    subarea = models.ForeignKey(Subarea, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']
