from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Cidade
from fabricaNode.serializers import CidadeSerializer


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
