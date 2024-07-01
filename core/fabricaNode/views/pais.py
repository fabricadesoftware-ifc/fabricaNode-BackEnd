from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Pais
from core.fabricaNode.serializers import PaisSerializer


class PaisViewSet(ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
