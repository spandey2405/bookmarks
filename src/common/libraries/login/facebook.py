import requests
from src.common.libraries.constants import *
from django.core import exceptions
from rest_framework.status import HTTP_400_BAD_REQUEST
from src.common.libraries.login.messages import *


class LoginFacebook():


    def __init__(self, **kwargs):
        self.auth = kwargs["auth"]
        self.id   = kwargs["id"]

    @property
    def login_via_fb(self):
        data_now = self.check_information()
        return data_now

    def check_information(self):
        """
        :param token: facebook token
        :return: facebook data @todo map data here or error
        """
        try:
            URL = '{0}{1}{2}'.format(FB_LOGIN_URL, FB_API_LOGIN_FIELDS, self.auth)
            data = requests.get(URL)
            if data.json()["id"] == self.id:
                # {u'email': u'spandey2405@gmail.com', u'id': u'1800004813592664', u'name': u'Saurabh Pandey'}
                return data.json()
            else:
                raise exceptions.ValidationError(INVALID_FB_TOKEN, code=HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise exceptions.ValidationError(INVALID_FB_TOKEN, code=HTTP_400_BAD_REQUEST)
