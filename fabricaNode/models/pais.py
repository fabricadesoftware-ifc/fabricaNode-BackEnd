from django.db import models

class pais(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nome']