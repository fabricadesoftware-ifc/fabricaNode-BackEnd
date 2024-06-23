from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Cidade
from core.fabricaNode.serializers import CidadeSerializer


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
