from django.db import models

from .cidade import cidade
from .subarea import subarea


class autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    dataNascimento = models.DateField()
    cidade = models.ForeignKey(cidade, on_delete=models.RESTRICT)
    subarea = models.ForeignKey(subarea, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']
