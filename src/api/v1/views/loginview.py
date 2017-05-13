from rest_framework import generics
from rest_framework  import mixins
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from src.api.v1.libraries.customresponse import CustomResponse
from src.api.v1.libraries.loggingmixin import LoggingMixin
from django_mysqlpool import auto_close_db
from src.common.libraries.login import LoginLibrary
from src.common.models.user import User
from django.core import exceptions
from src.common.libraries.login.messages import *
from django.core import exceptions as django_exc

'''
{
"login_type": "google/facebook/email",
"user_id": "Email/Facebook_id/Google_Id",
"auth":"Password_Hash/facebook_token/google_token"
}


{
  "message": "logged in",
  "payload": {
    "name": "Saurabh Pandey",
    "email": "spandey2405@gmail.com",
    "pro_pic": "NA",
    "google_id": "NA",
    "google_link": "NA",
    "facebook_id": "1800004813592664",
    "facebook_link": "NA",
    "user_id": "dd027c1d-cfbb-470f-9c04-34df6dcef6c7",
    "created": "2017-04-30T22:53:58.662714",
    "updated": "2017-04-30T22:53:58.662786",
    "is_verified": false,
    "access_token": "3f5518421233b7a4e013cea7fdb8835a50d8a6b7"
  },
  "success": true
}

'''

class LoginView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = User

    @auto_close_db
    def post(self, request):
        fb_id       = False
        google_id   = False
        email       = False
        password    = False
        
        login_details = request.data.copy()

        login_type = login_details.get("login_type", False)
        user_id = login_details.get("user_id", False)
        auth = login_details.get("auth", False)

        if login_type == False:
            raise django_exc.ValidationError(TYPE_LOGIN_NOT_FOUND, code=HTTP_400_BAD_REQUEST)
        if user_id == False:
            raise django_exc.ValidationError(USER_ID_NOT_FOUND, code=HTTP_400_BAD_REQUEST)
        if auth == False:
            raise django_exc.ValidationError(AUTH_NOT_FOUND, code=HTTP_400_BAD_REQUEST)
        
        if login_type == "google":
            google_id   = user_id
        elif login_type == "facebook":
            fb_id       = user_id
        elif login_type == "email":
            email       = user_id
            password    = auth
        else:
            raise django_exc.ValidationError(UNKNOWN_LOGIN_TYPE, code=HTTP_400_BAD_REQUEST)

        print "Login Type", login_type, "google id", google_id
        print "Facebook_id", fb_id, "auth", auth
        print "\n"
        response, message = LoginLibrary(
            fb_id=fb_id,
            google_id=google_id,
            auth=auth,
            email=email,
            password=password
        ).login

        return CustomResponse(message=message, payload=response, code=HTTP_201_CREATED)