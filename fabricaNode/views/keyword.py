from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Keyword
from fabricaNode.serializers import KeywordSerializer


class KeywordViewSet(ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer