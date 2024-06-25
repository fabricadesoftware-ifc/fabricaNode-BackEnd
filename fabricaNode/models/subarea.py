from django.db import models

from .area import Area


class Subarea(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    area = models.ForeignKey(Area, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Subárea'
        verbose_name_plural = 'Subáreas'
        ordering = ['nome']
