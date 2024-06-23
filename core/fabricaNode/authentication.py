# from django.core.exceptions import ObjectDoesNotExist
# from django.conf import settings
# from rest_framework import authentication
# from rest_framework.exceptions import AuthenticationFailed

# from passageidentity import Passage, PassageError
# from passageidentity.openapi_client.models import UserInfo

# from core.fabricaNode.models import User

# PASSAGE_APP_ID = settings.PASSAGE_APP_ID
# PASSAGE_API_KEY = settings.PASSAGE_API_KEY
# PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY
# psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY, auth_strategy=PASSAGE_AUTH_STRATEGY)


# class TokenAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request) -> tuple[User, None]:
#         auth_header: str = request.headers.get("Authorization")
#         if not auth_header:
#             return None

#         try:
#             psg_user_id: str = psg.authenticateRequest(request)
#         except PassageError as e:
#             raise AuthenticationFailed(e.message) from e

#         try:
#             user: User = User.objects.get(passage_id=psg_user_id)
#         except ObjectDoesNotExist:
#             psg_user: UserInfo = psg.getUser(psg_user_id)
#             user: User = User.objects.create_user(
#                 passage_id=psg_user.id,
#                 email=psg_user.email,
#             )

#         return (user, None)