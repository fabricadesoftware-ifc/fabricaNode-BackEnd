from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Publicacao_keyword
from core.fabricaNode.serializers import Publicacao_keywordSerializer


class Publicacao_keywordViewSet(ModelViewSet):
    queryset = Publicacao_keyword.objects.all()
    serializer_class = Publicacao_keywordSerializer