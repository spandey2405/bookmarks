from django.core import exceptions
from rest_framework.status import HTTP_400_BAD_REQUEST
from src.common.libraries.login.messages import *
from src.common.libraries.login.facebook import LoginFacebook
from src.common.libraries.login.google import LoginGoogle
from src.api.v1.serializers.usersserializer import User, UsersSerializer
from src.common.models.token import Token


class LoginLibrary():
    def __init__(self, **kwargs):
        self.fb_id = kwargs.get("fb_id", False)
        self.google_id = kwargs.get("google_id", False)
        self.auth = kwargs.get("auth", False)
        self.email = kwargs.get("email", False)
        self.password = kwargs.get("password", False)

    @property
    def login(self):
        if self.auth:
            if self.fb_id:

                data_now = LoginFacebook(auth=self.auth, id=self.fb_id).login_via_fb
                print "Data from facebook", data_now

            elif self.google_id:
                data_now = LoginGoogle(auth=self.auth, id=self.google_id).login_via_google
                print "Data from Google", data_now
            else:
                raise exceptions.ValidationError(MISSING_SOCIAL_LOGIN_ID, code=HTTP_400_BAD_REQUEST)

        else:
            data_now = False
            if self.email and self.password:
                print "Run Email Password Type of login"
            else:
                print "id"

        if "email" not in data_now:
            if self.google_id:
                msg = "unable to get email from google, make sure your token has access to email info"
            else:
                msg = "unable to get email from facebook, make sure your token has access to email info"


            raise exceptions.ValidationError(msg, code=HTTP_400_BAD_REQUEST)

        try:
            token, created, user_info = self.get_create_user(data_now=data_now)
        except Exception as e:
            print e
            raise exceptions.ValidationError("Internal Server Error Please Try Again Later", code=HTTP_400_BAD_REQUEST)
        message = 'already logged in'
        if created:
            message = 'logged in'

        user_info["access_token"] = token

        return user_info, message


    def get_create_user(self, data_now):
        if self.google_id or self.fb_id:
            if User.objects.filter(email=data_now["email"]).exists():
                user = User.objects.get(email=data_now["email"])
                token, created = Token.objects.get_or_create(user=user)
                user_info = UsersSerializer(user).data

                if self.google_id and user_info["google_id"] == "Not Avalible":
                    User.objects.filter(email=data_now["email"]).update(google_id=self.google_id)
                    user_info["google_id"] = self.google_id

                if self.fb_id and user_info["facebook_id"] == "Not Avalible":
                    User.objects.filter(email=data_now["email"]).update(facebook_id=self.fb_id)
                    user_info["facebook_id"] = self.fb_id

            else:
                data = dict()
                data["email"]       = data_now["email"]
                if self.google_id:
                    data["google_id"]   = self.google_id
                else:
                    data["facebook_id"] = self.fb_id

                data["name"]        = data_now["name"]
                user = User.objects.create(**data)
                token, created = Token.objects.get_or_create(user=user)
                user_info = UsersSerializer(user).data

            return token.access_token, created, user_info

        else:
            raise exceptions.ValidationError(MISSING_SOCIAL_LOGIN_ID, code=HTTP_400_BAD_REQUEST)