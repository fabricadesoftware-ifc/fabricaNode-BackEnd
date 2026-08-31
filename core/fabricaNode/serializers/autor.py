from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.fabricaNode.models import Autor


class AutorSerializer(ModelSerializer):
    is_favorito = SerializerMethodField()

    class Meta:
        model = Autor
        fields = "__all__"

    def get_is_favorito(self, obj):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            return False
        return obj.favoritos.filter(pk=user.pk).exists()
