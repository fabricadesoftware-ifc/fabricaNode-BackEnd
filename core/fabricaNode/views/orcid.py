from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.fabricaNode.integrations import orcid
from core.fabricaNode.integrations.keywords import buscar_keywords
from core.fabricaNode.models import Autor, Keyword, Publicacao


class OrcidBuscarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        nome = request.query_params.get("nome", "").strip()
        if not nome:
            return Response(
                {"detail": "Parâmetro 'nome' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(orcid.buscar_por_nome(nome))


class OrcidObrasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, orcid_id):
        return Response(orcid.listar_obras(orcid_id))


class OrcidConfirmarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        orcid_id = request.data.get("orcid_id")
        put_codes = set(request.data.get("obras", []))

        if not orcid_id:
            return Response(
                {"detail": "'orcid_id' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        usuario = request.user
        nome, _, sobrenome = usuario.name.partition(" ")

        autor, _ = Autor.objects.get_or_create(
            usuario=usuario,
            defaults={"nome": nome, "sobrenome": sobrenome, "email": usuario.email},
        )
        autor.orcid_id = orcid_id
        autor.save()

        obras_importadas = []
        for obra in orcid.listar_obras(orcid_id):
            if obra["put_code"] not in put_codes:
                continue

            publicacao, criada = Publicacao.objects.get_or_create(
                titulo=obra["titulo"],
                defaults={
                    "dataPublicacao": int(obra["ano"]) if obra["ano"] else 0,
                    "url": obra["url"],
                    "abstract": "",
                    "conferencia": "",
                    "tipo": orcid.TIPO_POR_ORCID.get(obra["tipo"], "OUTRO"),
                },
            )
            publicacao.autor.add(autor)

            if criada:
                palavras = buscar_keywords(obra["url"])
                if palavras:
                    keywords = [
                        Keyword.objects.get_or_create(palavra=palavra)[0]
                        for palavra in palavras
                    ]
                    publicacao.keyword.set(keywords)

            obras_importadas.append(publicacao.id)

        return Response(
            {"autor_id": autor.id, "publicacoes_importadas": obras_importadas},
            status=status.HTTP_200_OK,
        )
