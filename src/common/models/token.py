import binascii, os
from django.db import models

from src.common.libraries.constants import *
from src.common.models.user import User
from django.core import exceptions as django_exc


class TokenManager(models.Manager):

    def generate_access_token(self):
        return binascii.hexlify(os.urandom(TOKEN_LENGTH/2)).decode()

    def get_access_token(self, user_id=None, access_token=None):
        if user_id:
            return Token.objects.get(user_id=user_id)
        elif access_token:
            return Token.objects.get(access_token=access_token)
        raise django_exc.ObjectDoesNotExist('access token object does not exists')

class Token(models.Model):
    access_token = models.CharField(max_length=TOKEN_LENGTH, primary_key=True)
    user = models.ForeignKey(User)
    ts_created = models.DateTimeField(auto_now_add=True)
    objects = TokenManager()

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = Token.objects.generate_access_token()
        return super(Token, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.access_token

    class Meta:
        db_table = 'userToken'
        app_label = 'common'