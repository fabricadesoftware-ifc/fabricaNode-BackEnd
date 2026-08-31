from django.core.management.base import BaseCommand

from core.fabricaNode.models import Area, Cidade, Estado, Keyword, Pais

CATEGORIAS = [
    ("Informatica", "#0029B9"),
    ("Quimica", "#C3A8E5"),
    ("Agropecuaria", "#DB9FC6"),
    ("Termodinamica", "#418935"),
    ("Medicina", "#29006C"),
    ("Robotica", "#0029B9"),
    ("Seguranca", "#C3A8E5"),
    ("Redes", "#29006C"),
    ("Computacao", "#418935"),
    ("Matematica", "#DB9FC6"),
    ("Inteligencia artificial", "#418935"),
    ("Economia", "#0029B9"),
    ("Engenharia", "#C3A8E5"),
    ("Urbanismo", "#418935"),
    ("Meio ambiente", "#29006C"),
]

KEYWORDS = [
    "algoritmos", "genéticos", "otimização",
    "inteligência artificial", "machine learning", "redes neurais",
    "medicina", "diagnóstico", "previsão de mercado",
    "finanças", "deep learning", "processamento de imagem",
    "visão computacional", "sistemas embarcados", "internet das coisas",
    "IoT", "big data", "análise de dados",
    "tempo real", "blockchain", "segurança da informação",
    "criptografia", "computação quântica", "algoritmos quânticos",
    "futuro da computação", "aprendizado supervisionado", "classificação",
    "segurança em redes", "firewall", "detecção de intrusão",
    "smart cities", "tecnologias emergentes", "sustentabilidade",
    "redes de sensores", "comunicação sem fio", "agricultura",
    "tecnologia agrícola", "protocolo seguro", "robótica",
    "energia sustentável", "tecnologias verdes", "meio ambiente",
]


class Command(BaseCommand):
    help = (
        "Popula o banco com a base geográfica (Brasil/SC/Araquari) e a "
        "taxonomia de áreas/keywords usada pra categorizar publicações. "
        "Autores reais vêm de seed_professores; publicações reais, do "
        "ORCID (core/fabricaNode/views/orcid.py)."
    )

    def handle(self, *args, **options):
        pais, _ = Pais.objects.get_or_create(sigla="BR", defaults={"nome": "Brasil"})
        estado, _ = Estado.objects.get_or_create(
            sigla="SC", pais=pais, defaults={"nome": "Santa Catarina"}
        )
        Cidade.objects.get_or_create(nome="Araquari", estado=estado)

        for nome, cor in CATEGORIAS:
            Area.objects.get_or_create(nome=nome, defaults={"cor": cor})

        for palavra in KEYWORDS:
            Keyword.objects.get_or_create(palavra=palavra)

        self.stdout.write(self.style.SUCCESS(
            f"Seed concluído: {len(CATEGORIAS)} áreas, {len(KEYWORDS)} keywords."
        ))
