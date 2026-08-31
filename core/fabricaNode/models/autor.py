from django.conf import settings
from django.db import models

from .cidade import Cidade
from .subarea import Subarea


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    dataNascimento = models.IntegerField(null=True, blank=True)
    cidade = models.ForeignKey(
        Cidade, on_delete=models.RESTRICT, null=True, blank=True
    )
    subarea = models.ForeignKey(
        Subarea, on_delete=models.RESTRICT, null=True, blank=True
    )
    favoritos = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="autores_favoritos", blank=True
    )

    # Terreno para a integração futura com fontes externas (Lattes, ORCID,
    # ResearchGate, Academia.edu, Google Scholar). Preenchido só quando o
    # usuário confirmar a autoria de uma publicação encontrada nessas fontes.
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="autor_perfil",
    )
    lattes_id = models.CharField(max_length=255, null=True, blank=True)
    orcid_id = models.CharField(max_length=255, null=True, blank=True)
    researchgate_id = models.CharField(max_length=255, null=True, blank=True)
    academia_edu_id = models.CharField(max_length=255, null=True, blank=True)
    google_scholar_id = models.CharField(max_length=255, null=True, blank=True)
    openalex_id = models.CharField(max_length=255, null=True, blank=True)

    # Preenchido para autores importados do portal da Fábrica de Software
    # (core/fabricaNode/integrations/portal.py). portal_member_id é o id
    # estável do membro na API do portal, usado pra evitar duplicar no reseed.
    portal_member_id = models.IntegerField(null=True, blank=True, unique=True)
    biografia = models.TextField(blank=True, default="")
    foto_url = models.URLField(blank=True, default="")
    linkedin = models.URLField(blank=True, default="")
    github = models.URLField(blank=True, default="")
    instagram = models.URLField(blank=True, default="")

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nome"]
