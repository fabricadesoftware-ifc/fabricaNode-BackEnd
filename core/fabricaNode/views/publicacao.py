from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Publicacao
from core.fabricaNode.serializers import PublicacaoSerializer


class PublicacaoViewSet(ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer