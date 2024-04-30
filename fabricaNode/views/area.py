from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import area
from fabricaNode.serializers import AreaSerializer


class AreaViewSet(ModelViewSet):
    queryset = area.objects.all()
    serializer_class = AreaSerializer