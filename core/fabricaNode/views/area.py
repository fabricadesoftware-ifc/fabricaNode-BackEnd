from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Area
from core.fabricaNode.serializers import AreaSerializer


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer