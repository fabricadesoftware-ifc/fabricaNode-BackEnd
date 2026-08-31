from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.fabricaNode.models import Publicacao


class PublicacaoSerializer(ModelSerializer):
    is_favorito = SerializerMethodField()

    class Meta:
        model = Publicacao
        fields = "__all__"

    def get_is_favorito(self, obj):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            return False
        return obj.favoritos.filter(pk=user.pk).exists()
