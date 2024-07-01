from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Estado
from core.fabricaNode.serializers import EstadoSerializer


class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer