import requests

ORCID_API_BASE = "https://pub.orcid.org/v3.0"

# Mapeia os tipos de obra do ORCID pros choices de Publicacao.tipo.
# https://info.orcid.org/documentation/integration-guide/orcid-work-types/
TIPO_POR_ORCID = {
    "journal-article": "FULLP",
    "conference-paper": "FULLP",
    "conference-abstract": "RESUM",
    "book": "LIVRO",
    "book-chapter": "CAPLI",
    "dissertation-thesis": "TESES",
    "report": "RELAT",
}


def buscar_por_nome(nome: str) -> list[dict]:
    response = requests.get(
        f"{ORCID_API_BASE}/expanded-search/",
        params={"q": nome, "rows": 10},
        headers={"Accept": "application/json"},
        timeout=10,
    )
    response.raise_for_status()
    resultados = response.json().get("expanded-result") or []

    return [
        {
            "orcid_id": item["orcid-id"],
            "nome": item.get("credit-name")
            or f"{item.get('given-names', '')} {item.get('family-names', '')}".strip(),
            "instituicoes": item.get("institution-name", []),
        }
        for item in resultados
    ]


def listar_obras(orcid_id: str) -> list[dict]:
    response = requests.get(
        f"{ORCID_API_BASE}/{orcid_id}/works",
        headers={"Accept": "application/json"},
        timeout=10,
    )
    response.raise_for_status()

    obras = []
    for grupo in response.json().get("group", []):
        resumo = grupo["work-summary"][0]
        ano = ((resumo.get("publication-date") or {}).get("year") or {}).get("value")

        obras.append(
            {
                "put_code": resumo["put-code"],
                "titulo": resumo["title"]["title"]["value"],
                "ano": ano,
                "tipo": resumo.get("type"),
                "url": _extrair_url(resumo),
            }
        )
    return obras


def _extrair_url(resumo: dict) -> str:
    external_ids = (resumo.get("external-ids") or {}).get("external-id", [])
    for external_id in external_ids:
        if external_id.get("external-id-type") == "doi":
            return f"https://doi.org/{external_id['external-id-value']}"

    url = resumo.get("url")
    if isinstance(url, dict):
        return url.get("value") or ""
    return url or ""
