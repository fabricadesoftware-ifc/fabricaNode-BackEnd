from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Area
from fabricaNode.serializers import AreaSerializer


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer