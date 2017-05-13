import requests
from django.core import exceptions
from rest_framework.status import HTTP_400_BAD_REQUEST
from src.common.libraries.login.messages import *
from src.api.v1.serializers.usersserializer import User

class LoginGoogle():


    def __init__(self, **kwargs):
        self.auth = kwargs["auth"]
        self.id   = kwargs["id"]
        self.user_data = self.check_information()

    @property
    def login_via_google(self):
        data_now = self.check_information()
        return data_now

    def check_information(self):
        """
        :param token: Google token
        :return: Google data @todo map data here or error
        """
        try:
            URL = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token={0}'.format(self.auth)
            data = requests.get(URL)
            if data.json()["id"] == self.id:
                return data.json()
            else:
                raise exceptions.ValidationError(INVALID_GOOGLE_TOKEN, code=HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise exceptions.ValidationError(INVALID_GOOGLE_TOKEN, code=HTTP_400_BAD_REQUEST)
