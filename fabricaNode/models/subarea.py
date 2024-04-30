from django.db import models

from .area import Area


class subarea(models.Model):
    nome = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Subárea'
        verbose_name_plural = 'Subáreas'
        ordering = ['nome']
