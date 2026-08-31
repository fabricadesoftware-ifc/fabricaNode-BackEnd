from . import openalex
from .scraper import extrair_keywords


def buscar_keywords(url: str) -> list[str]:
    """
    Tenta achar keywords pra uma publicação a partir da sua URL, na ordem:
    1. OpenAlex (via DOI) — não depende do site da editora, cobre até os
       DOIs de editora que bloqueiam scraping direto (IEEE, Elsevier, etc).
    2. Scraping da meta tag citation_keywords da própria página — fallback
       pra quando não é DOI ou a OpenAlex não tem o registro.

    Lista vazia se não achar em nenhuma das duas (URL vazia, publicação sem
    keyword disponível em lugar nenhum).
    """
    if not url:
        return []

    palavras = openalex.buscar_keywords_por_doi(url)
    if palavras:
        return palavras

    return extrair_keywords(url)
