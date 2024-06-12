from rest_framework.serializers import ModelSerializer

from fabricaNode.models import Editora


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'