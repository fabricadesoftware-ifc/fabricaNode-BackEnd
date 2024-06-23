from rest_framework.serializers import ModelSerializer

from core.fabricaNode.models import Publicacao_keyword


class Publicacao_keywordSerializer(ModelSerializer):
    class Meta:
        model = Publicacao_keyword
        fields = '__all__'