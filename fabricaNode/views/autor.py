from rest_framework.viewsets import ModelViewSet

from fabricaNode.models import Autor
from fabricaNode.serializers.autor import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer