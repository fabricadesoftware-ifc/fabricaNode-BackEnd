from rest_framework.serializers import ModelSerializer

from fabricaNode.models import Cidade


class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'