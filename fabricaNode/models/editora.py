from django.db import models

from .cidade import cidade

class editora(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(cidade, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']
