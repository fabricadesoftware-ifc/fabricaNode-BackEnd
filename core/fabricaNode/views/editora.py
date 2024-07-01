from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Editora
from core.fabricaNode.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer