from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Pais
from fabricaNode.serializers import PaisSerializer


class PaisViewSet(ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
