from rest_framework.serializers import ModelSerializer

from fabricaNode.models import Publicacao


class PublicacaoSerializer(ModelSerializer):
    class Meta:
        model = Publicacao
        fields = '__all__'