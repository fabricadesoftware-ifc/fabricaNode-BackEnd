from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class FavoritarMixin:
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def favoritar(self, request, pk=None):
        obj = self.get_object()
        user = request.user

        if obj.favoritos.filter(pk=user.pk).exists():
            obj.favoritos.remove(user)
            is_favorito = False
        else:
            obj.favoritos.add(user)
            is_favorito = True

        return Response({"is_favorito": is_favorito}, status=status.HTTP_200_OK)
