from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.fabricaNode.integrations import openalex
from core.fabricaNode.models import Autor, Keyword, Publicacao


class OpenAlexBuscarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        nome = request.query_params.get("nome", "").strip()
        if not nome:
            return Response(
                {"detail": "Parâmetro 'nome' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(openalex.buscar_autores_por_nome(nome))


class OpenAlexObrasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, openalex_id):
        return Response(openalex.listar_obras_por_autor(openalex_id))


class OpenAlexConfirmarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        openalex_id = request.data.get("openalex_id")
        openalex_work_ids = set(request.data.get("obras", []))

        if not openalex_id:
            return Response(
                {"detail": "'openalex_id' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        usuario = request.user
        nome, _, sobrenome = usuario.name.partition(" ")

        autor, _ = Autor.objects.get_or_create(
            usuario=usuario,
            defaults={"nome": nome, "sobrenome": sobrenome, "email": usuario.email},
        )
        autor.openalex_id = openalex_id
        autor.save()

        obras_importadas = []
        for obra in openalex.listar_obras_por_autor(openalex_id):
            if obra["openalex_id"] not in openalex_work_ids:
                continue

            publicacao, criada = Publicacao.objects.get_or_create(
                titulo=obra["titulo"],
                defaults={
                    "dataPublicacao": obra["ano"] or 0,
                    "url": obra["url"],
                    "abstract": "",
                    "conferencia": "",
                    "tipo": openalex.TIPO_POR_OPENALEX.get(obra["tipo"], "OUTRO"),
                },
            )
            publicacao.autor.add(autor)

            if criada and obra["keywords"]:
                keywords = [
                    Keyword.objects.get_or_create(palavra=palavra)[0]
                    for palavra in obra["keywords"]
                ]
                publicacao.keyword.set(keywords)

            obras_importadas.append(publicacao.id)

        return Response(
            {"autor_id": autor.id, "publicacoes_importadas": obras_importadas},
            status=status.HTTP_200_OK,
        )
