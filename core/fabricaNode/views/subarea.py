from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Subarea
from core.fabricaNode.serializers import SubareaSerializer


class SubareaViewSet(ModelViewSet):
    queryset = Subarea.objects.all()
    serializer_class = SubareaSerializer