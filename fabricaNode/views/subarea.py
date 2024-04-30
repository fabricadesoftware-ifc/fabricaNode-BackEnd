from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Subarea
from fabricaNode.serializers import SubareaSerializer


class SubareaViewSet(ModelViewSet):
    queryset = Subarea.objects.all()
    serializer_class = SubareaSerializer