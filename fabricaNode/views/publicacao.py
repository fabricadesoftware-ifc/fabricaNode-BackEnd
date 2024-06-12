from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Publicacao
from fabricaNode.serializers import PublicacaoSerializer


class PublicacaoViewSet(ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer