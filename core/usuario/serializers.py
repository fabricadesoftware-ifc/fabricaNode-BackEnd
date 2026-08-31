from rest_framework.serializers import ModelSerializer

from .models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "email", "name", "is_staff", "is_active", "date_joined")
        read_only_fields = ("id", "is_staff", "is_active", "date_joined")


class UsuarioRegisterSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "email", "name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)
