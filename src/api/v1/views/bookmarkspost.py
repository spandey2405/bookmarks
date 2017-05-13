from rest_framework import generics
from rest_framework  import mixins
from rest_framework.status import HTTP_201_CREATED
from src.api.v1.libraries.customresponse import CustomResponse
from src.api.v1.libraries.loggingmixin import LoggingMixin
from django_mysqlpool import auto_close_db
from src.api.v1.serializers.bookmarksserializser import Bookmarks, BookmarksSerializer
from src.common.libraries.bookmarks import BookmarksLib
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
'''
POST VERSION :

data = {
    "post_title": "TITLE_OF_BOOKMARK",
    "post_image": "IMAGE_URL",
    "post_by": "ID_OF_PERSON",
    "post_description": "DESCIPTION",
    "privacy": "0 for public and 1 for private",
    "user_id": "user_id"
}
'''


class BookmarksView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Bookmarks
    serializer_class = BookmarksSerializer

    @auto_close_db
    def post(self, request):
        data = request.data.copy()
        try:
            response = BookmarksLib(url=data['url']).add_post
        except Exception as e:
            print e
        return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)

    @auto_close_db
    def delete(self, request):
        id = request.data.copy()["id"]
        Bookmarks.objects.get(id=id).delete()
        response = {
            'Successfully Deleted'
        }
        return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)