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

class estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(pais, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.sigla}-{self.nome}'
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['sigla']

class cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(estado, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.nome}({self.estado.sigla})'
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']

class autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    dataNascimento = models.DateField()
    cidade = models.ForeignKey(cidade, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']

class editora(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(cidade, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']

class publicacao(models.Model):
    titulo = models.CharField(max_length=150)
    dataPublicacao = models.DateField()
    autor = models.ManyToManyField(autor)
    editora = models.ForeignKey(editora, on_delete=models.RESTRICT)
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

class keyword(models.Model):
    palavra = models.CharField(max_length=50)

    def __str__(self):
        return self.palavra
    
    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'
        ordering = ['palavra']

class publicacao_keyword(models.Model):
    publicacao = models.ForeignKey(publicacao, on_delete=models.RESTRICT)
    keyword = models.ForeignKey(keyword, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.publicacao.titulo} - {self.keyword.palavra}'
    
    class Meta:
        verbose_name = 'Publicação Keyword'
        verbose_name_plural = 'Publicações Keywords'
        ordering = ['publicacao']