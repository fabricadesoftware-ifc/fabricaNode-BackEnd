from django.db import models


class area(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
        ordering = ['nome']