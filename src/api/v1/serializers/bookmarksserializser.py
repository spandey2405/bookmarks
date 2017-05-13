from src.api.v1.serializers.dynamicfieldmodelserializer import DynamicFieldsModelSerializer
from src.common.models.bookmarks import Bookmarks
from src.api.v1.serializers.usersserializer import UsersSerializer, User


class BookmarksSerializer(DynamicFieldsModelSerializer):

    user_id = UsersSerializer()

    class Meta:
        model = Bookmarks
        fields = (
            "id",
            "title",
            "des",
            "image",
            "link",
            "keywords",
            "privacy",
            "user_id"
        )