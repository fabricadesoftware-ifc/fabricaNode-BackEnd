from django.core.management.base import BaseCommand

from core.fabricaNode.integrations.keywords import buscar_keywords
from core.fabricaNode.models import Keyword, Publicacao


class Command(BaseCommand):
    help = (
        "Preenche as keywords das publicações que não têm nenhuma (útil "
        "pra dados antigos importados antes de isso ser automático). "
        "Publicações novas do ORCID já ganham keyword na hora, via "
        "core/fabricaNode/views/orcid.py. Melhor esforço: nem toda "
        "publicação tem keyword disponível em algum lugar."
    )

    def handle(self, *args, **options):
        publicacoes = list(Publicacao.objects.filter(keyword__isnull=True).exclude(url=""))
        total = len(publicacoes)

        enriquecidas = 0
        for publicacao in publicacoes:
            palavras = buscar_keywords(publicacao.url)
            if not palavras:
                continue

            keywords = [
                Keyword.objects.get_or_create(palavra=palavra)[0]
                for palavra in palavras
            ]
            publicacao.keyword.set(keywords)
            enriquecidas += 1
            self.stdout.write(f"  {publicacao.titulo[:60]}: {', '.join(palavras)}")

        self.stdout.write(
            self.style.SUCCESS(
                f"Concluído: {enriquecidas}/{total} publicações "
                f"ganharam keywords."
            )
        )
