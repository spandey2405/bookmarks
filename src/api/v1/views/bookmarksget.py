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


class BookmarksPagination(PageNumberPagination):
    page_size=10
    page_size_query_param = 'page_size'


class BookmarksGETView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = Bookmarks
    serializer_class = BookmarksSerializer
    pagination_class = BookmarksPagination

    @auto_close_db

    def post(self, request):
        if "search_key" in request.GET.copy():
            search_key = request.GET.copy()['search_key']
            coupons = Bookmarks.objects.filter(name__contains=search_key)
        else:
            coupons = Bookmarks.objects.all()

        page = self.paginate_queryset(coupons)
        if page is not None:
            serializer = BookmarksSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BookmarksSerializer(coupons, many=True)
        return CustomResponse(message='Success', payload=serializer.data, code=HTTP_201_CREATED)

    # @auto_close_db
    # def post(self, request):
    #     data = request.data.copy()
    #     try:
    #         response = BookmarksLib(url=data['url']).add_post
    #     except Exception as e:
    #         print e
    #     return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)
    #
    # @auto_close_db
    # def put(self, request):
    #     response = {
    #         'welcome to Bookmarks api version v1 PUT View'
    #     }
    #     return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)
    #
    # @auto_close_db
    # def delete(self, request):
    #     response = {
    #         'welcome to Bookmarks api version v1 Delete View'
    #     }
    #     return CustomResponse(message='Success', payload=response, code=HTTP_201_CREATED)