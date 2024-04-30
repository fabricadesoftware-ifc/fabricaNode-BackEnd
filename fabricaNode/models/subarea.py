from django.db import models

from .area import area


class subarea(models.Model):
    nome = models.CharField(max_length=50)
    area = models.ForeignKey(area, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Subárea'
        verbose_name_plural = 'Subáreas'
        ordering = ['nome']
