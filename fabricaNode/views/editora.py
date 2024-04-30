from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Editora
from fabricaNode.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer