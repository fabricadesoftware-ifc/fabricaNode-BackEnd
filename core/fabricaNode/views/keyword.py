from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Keyword
from core.fabricaNode.serializers import KeywordSerializer


class KeywordViewSet(ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer