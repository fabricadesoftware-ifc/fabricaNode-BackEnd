# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet

# from core.fabricaNode.authentication import TokenAuthentication
# from core.fabricaNode.models.user import User
# from core.fabricaNode.serializers.user import UserSerializer


# from firebase_admin.messaging import Message
# from fcm_django.models import FCMDevice


# class AuthTokenView(APIView):
#     authentication_classes = [TokenAuthentication]

#     @staticmethod
#     def post(request):
#         user = request.user
#         passage_user_id = user.passage_id
#         return Response(
#             {"authStatus": "success", "id": user.id, "passage_id": user.passage_id}, status=status.HTTP_200_OK
#         )


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @action(detail=False, methods=["post"])
#     def send(self, request):
#         # You can still use .filter() or any methods that return QuerySet (from the chain)
#         device = FCMDevice.objects.all().first()
#         # send_message parameters include: message, dry_run, app
#         device.send_message(Message(data={...}))
#         return Response({"message": "Hello, World!"})

#     # @action(detail=False, methods=["post"])
#     # def register(self, request):