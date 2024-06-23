from rest_framework.serializers import ModelSerializer

from core.fabricaNode.models import Keyword


class KeywordSerializer(ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'