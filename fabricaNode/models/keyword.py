from django.db import models


class Keyword(models.Model):
    palavra = models.CharField(max_length=50)

    def __str__(self):
        return self.palavra
    
    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'
        ordering = ['palavra']
