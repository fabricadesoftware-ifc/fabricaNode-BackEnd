from rest_framework.serializers import ModelSerializer

from fabricaNode.models import area


class AreaSerializer(ModelSerializer):
    class Meta:
        model = area
        fields = '__all__'