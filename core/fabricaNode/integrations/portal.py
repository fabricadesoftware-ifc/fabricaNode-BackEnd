import requests

PORTAL_API_URL = "https://portal-api.fabricadesoftware.ifc.edu.br/api/members/"


def buscar_membros(tipo: str | None = None) -> list[dict]:
    response = requests.get(PORTAL_API_URL, timeout=10)
    response.raise_for_status()
    membros = response.json()

    if tipo:
        membros = [membro for membro in membros if membro.get("type") == tipo]

    return [
        {
            "portal_id": membro["id"],
            "nome": membro["name"],
            "biografia": membro.get("biography") or "",
            "foto_url": (membro.get("image") or {}).get("file") or "",
            "linkedin": membro.get("linkedin") or "",
            "github": membro.get("github") or "",
            "instagram": membro.get("instagram") or "",
        }
        for membro in membros
    ]
