from rest_framework.serializers import ModelSerializer

from core.fabricaNode.models import Estado


class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'