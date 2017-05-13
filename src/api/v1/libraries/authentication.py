from src.common.models import User, Token
from rest_framework import authentication
from rest_framework import exceptions
from src.common.libraries.constants import *

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token_from_header = request.META.get(KEY_TOKEN)
        if not token_from_header:
            return None
        if Token.objects.filter(access_token=token_from_header):
            token = Token.objects.get_access_token(access_token=token_from_header)
            user_id = token.user_id
            user = User.objects.get(user_id=user_id)
            return (user, token)
        raise exceptions.AuthenticationFailed('Invalid access token')

    def authenticate_header(self, request):
        return ['token','admin']