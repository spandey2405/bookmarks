from src.api.v1.serializers.bookmarksserializser import *
from django.core.exceptions import ValidationError
from src.common.libraries.scrapping.get_web_info import get_info

class BookmarksLib():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.url    = kwargs.get("url", False)
        self.user   = kwargs.get("user", False)

    @property
    def add_post(self):
        if not self.url:
            raise ValidationError("Invalid URL")

        info = get_info(url=self.url)
        print info
        if not self.user:
            info["user_id"] = self.get_default_user()



        return BookmarksSerializer(Bookmarks.objects.create(**info)).data

    def get_default_user(self):
        return User.objects.get(user_id="dd027c1d-cfbb-470f-9c04-34df6dcef6c7")

