from django.core.management.base import BaseCommand

from core.fabricaNode.integrations import portal
from core.fabricaNode.models import Autor, Publicacao

# Fingerprint do dataset fake criado por seed_demo_data (todas as publicações
# fake compartilham essa mesma URL de exemplo, todos os autores fake
# compartilham esse mesmo email de exemplo).
URL_PUBLICACAO_FAKE = "http://copec.eu/congresses/intertech2014/proc/works/101.pdf"
EMAIL_AUTOR_FAKE = "julia@gmail.com"


class Command(BaseCommand):
    help = (
        "Remove o dataset fake de autores/publicações de exemplo e importa "
        "os professores reais da Fábrica de Software a partir do portal "
        "(https://portal-api.fabricadesoftware.ifc.edu.br/api/members/)."
    )

    def handle(self, *args, **options):
        publicacoes_removidas, _ = Publicacao.objects.filter(
            url=URL_PUBLICACAO_FAKE
        ).delete()
        autores_removidos, _ = Autor.objects.filter(email=EMAIL_AUTOR_FAKE).delete()

        criados = 0
        for membro in portal.buscar_membros(tipo="Docente"):
            nome, _, sobrenome = membro["nome"].partition(" ")
            _, created = Autor.objects.update_or_create(
                portal_member_id=membro["portal_id"],
                defaults={
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "email": "",
                    "biografia": membro["biografia"],
                    "foto_url": membro["foto_url"],
                    "linkedin": membro["linkedin"],
                    "github": membro["github"],
                    "instagram": membro["instagram"],
                },
            )
            if created:
                criados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Removidos: {autores_removidos} autores fake, "
                f"{publicacoes_removidas} publicações fake. "
                f"Importados/atualizados {criados} professores novos do portal."
            )
        )
