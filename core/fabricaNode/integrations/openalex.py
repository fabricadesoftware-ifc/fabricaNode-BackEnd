import requests

OPENALEX_API_BASE = "https://api.openalex.org"

# Mapeia os tipos de obra da OpenAlex pros choices de Publicacao.tipo.
TIPO_POR_OPENALEX = {
    "article": "FULLP",
    "conference-paper": "FULLP",
    "book": "LIVRO",
    "book-chapter": "CAPLI",
    "dissertation": "TESES",
    "report": "RELAT",
}


def _extrair_keywords(obra: dict) -> list[str]:
    return [
        keyword["display_name"]
        for keyword in obra.get("keywords", [])
        if keyword.get("display_name")
    ]


def buscar_keywords_por_doi(doi_url: str) -> list[str]:
    """
    Busca keywords de um trabalho na OpenAlex a partir do DOI. Cobre
    trabalhos cuja página de origem bloqueia scraping direto (IEEE,
    Elsevier, etc.) porque nunca precisa acessar o site da editora.
    """
    if "doi.org/" not in doi_url:
        return []

    try:
        response = requests.get(f"{OPENALEX_API_BASE}/works/{doi_url}", timeout=10)
        if response.status_code != 200:
            return []
        dados = response.json()
    except requests.RequestException:
        return []

    return _extrair_keywords(dados)


def buscar_autores_por_nome(nome: str) -> list[dict]:
    """
    Busca autores na OpenAlex por nome. Alternativa ao Lattes/Academia.edu
    (sem API oficial e protegidos por CAPTCHA/paywall) pra encontrar a
    produção de um pesquisador indexada internacionalmente.
    """
    try:
        response = requests.get(
            f"{OPENALEX_API_BASE}/authors",
            params={"search": nome, "per_page": 10},
            timeout=10,
        )
        response.raise_for_status()
        dados = response.json()
    except requests.RequestException:
        return []

    resultados = []
    for autor in dados.get("results", []):
        instituicoes = autor.get("last_known_institutions") or []
        resultados.append(
            {
                "openalex_id": autor["id"].removeprefix("https://openalex.org/"),
                "nome": autor["display_name"],
                "instituicoes": [i["display_name"] for i in instituicoes],
                "obras_count": autor.get("works_count", 0),
            }
        )
    return resultados


def listar_obras_por_autor(openalex_id: str) -> list[dict]:
    try:
        response = requests.get(
            f"{OPENALEX_API_BASE}/works",
            params={"filter": f"author.id:{openalex_id}", "per_page": 50},
            timeout=10,
        )
        response.raise_for_status()
        dados = response.json()
    except requests.RequestException:
        return []

    obras = []
    for obra in dados.get("results", []):
        localizacao = obra.get("primary_location") or {}
        obras.append(
            {
                "openalex_id": obra["id"].removeprefix("https://openalex.org/"),
                "titulo": obra.get("title") or obra.get("display_name") or "",
                "ano": obra.get("publication_year"),
                "tipo": obra.get("type"),
                "url": localizacao.get("landing_page_url") or obra.get("doi") or "",
                "keywords": _extrair_keywords(obra),
            }
        )
    return obras
