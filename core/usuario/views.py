from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.usuario.models import Usuario as User
from core.usuario.serializers import UsuarioRegisterSerializer, UsuarioSerializer


class UserViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all().order_by("id")
        if user.is_authenticated:
            return User.objects.filter(id=user.id).order_by("id")
        return User.objects.none()

    def get_serializer_class(self):
        if self.action == "create":
            return UsuarioRegisterSerializer
        return UsuarioSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
