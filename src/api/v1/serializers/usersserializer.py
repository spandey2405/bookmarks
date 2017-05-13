from src.api.v1.serializers.dynamicfieldmodelserializer import DynamicFieldsModelSerializer
from src.common.libraries.constants import *
from src.common.models.user import User
from rest_framework import serializers


class UsersSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = User
        fields = (
        "name",
        "email",
        "pro_pic",
        "google_id",
        "google_link",
        "facebook_id",
        "facebook_link",
        "user_id",
        "created",
        "updated",
        "is_verified"
        )