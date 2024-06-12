from django.db import models

from .autor import Autor
from .editora import Editora


class Publicacao(models.Model):
    titulo = models.CharField(max_length=150)
    dataPublicacao = models.DateField()
    autor = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete=models.RESTRICT, null=True, blank=True)
    conferencia = models.CharField(max_length=150)
    abstract = models.TextField()
    url = models.URLField()
    publicado_em = models.CharField(
        max_length=10,
        choices=[
            ('J', 'Journal'),
            ('C', 'Conferência'),
            ('L', 'Livro')
        ],
        default='J')
    abrangencia = models.CharField(
        max_length=3,
        choices=[
            ('INT', 'Internacional'),
            ('NAC', 'Nacional'),
            ('REG', 'Regional'),
            ('LOC', 'Local')
        ],
    )
    tipo = models.CharField(
        max_length=5,
        choices=[
            ('RESUM', 'Resumo Expandido'),
            ('FULLP', 'Full Paper'),
            ('LIVRO', 'Livro'),
            ('CAPLI', 'Capítulo de Livro'),
            ('TESES', 'Tese de Doutorado'),
            ('DISSE', 'Dissertação de Mestrado'),
            ('RELAT', 'Relatório Técnico'),
            ('MONOG', 'Trabalho de Conclusão de Curso'),
            ('OUTRO', 'Outro')
        ],
    )

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        ordering = ['titulo']
