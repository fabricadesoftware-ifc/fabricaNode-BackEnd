from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Estado
from fabricaNode.serializers import EstadoSerializer


class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer