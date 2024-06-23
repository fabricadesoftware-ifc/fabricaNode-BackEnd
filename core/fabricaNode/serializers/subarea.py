from rest_framework.serializers import ModelSerializer

from core.fabricaNode.models import Subarea


class SubareaSerializer(ModelSerializer):
    class Meta:
        model = Subarea
        fields = '__all__'