from rest_framework.viewsets import ModelViewSet

from core.fabricaNode.models import Autor
from core.fabricaNode.serializers.autor import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer