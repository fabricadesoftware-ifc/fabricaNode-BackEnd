import requests
from bs4 import BeautifulSoup

# Header de navegador real: sem isso, boa parte dos sites acadêmicos recusa a
# requisição (IEEE, por exemplo, devolve 202 vazio pra um User-Agent de bot).
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; FabricaNodeBot/1.0)"}


def extrair_keywords(url: str) -> list[str]:
    """
    Tenta extrair palavras-chave da página de uma publicação lendo a meta tag
    `citation_keywords` (padrão Highwire Press, usado pelo Google Scholar e
    adotado pela maioria dos repositórios acadêmicos — DSpace, SciELO, etc.).

    Nem toda página tem essa tag (editoras como IEEE/Elsevier costumam
    bloquear ou não expor), então isso é melhor-esforço: retorna lista vazia
    em qualquer falha, nunca levanta exceção.
    """
    if not url:
        return []

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all("meta", attrs={"name": "citation_keywords"})

    palavras = []
    for tag in tags:
        conteudo = tag.get("content", "")
        # Alguns sites mandam uma tag por keyword, outros mandam uma tag só
        # com todas separadas por ";" ou ",".
        for separador in (";", ","):
            if separador in conteudo:
                palavras.extend(parte.strip() for parte in conteudo.split(separador))
                break
        else:
            if conteudo.strip():
                palavras.append(conteudo.strip())

    # remove duplicadas mantendo a ordem
    vistas = set()
    unicas = []
    for palavra in palavras:
        chave = palavra.lower()
        if palavra and chave not in vistas:
            vistas.add(chave)
            unicas.append(palavra)

    return unicas
