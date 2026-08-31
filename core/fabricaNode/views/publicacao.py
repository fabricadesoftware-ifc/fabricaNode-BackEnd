from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.mixins import FavoritarMixin
from core.fabricaNode.models import Publicacao
from core.fabricaNode.serializers import PublicacaoSerializer


class PublicacaoViewSet(FavoritarMixin, ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
