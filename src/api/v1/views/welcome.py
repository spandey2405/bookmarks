from rest_framework import generics
from rest_framework  import mixins
from rest_framework.status import HTTP_201_CREATED
from src.api.v1.libraries.customresponse import CustomResponse
from src.api.v1.libraries.loggingmixin import LoggingMixin
from django_mysqlpool import auto_close_db

'''

'''

class WelcomeView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):

    @auto_close_db
    def get(self, request):
        response = {
            'welcome to Bookmarks api version v1 GET VIEW'
        }
        return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)

    @auto_close_db
    def post(self, request):
        response = {
            'welcome to Bookmarks api version v1 POST VIEW'
        }
        return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)

    @auto_close_db
    def put(self, request):
        response = {
            'welcome to Bookmarks api version v1 PUT View'
        }
        return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)

    @auto_close_db
    def delete(self, request):
        response = {
            'welcome to Bookmarks api version v1 Delete View'
        }
        return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)