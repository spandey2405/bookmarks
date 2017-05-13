from django.db import models
from src.common.models import User

class Bookmarks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    des = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    keywords = models.CharField(max_length=500)
    privacy = models.IntegerField(default=0)
    user_id = models.ForeignKey(User)

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        return super(Bookmarks, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'bookmarks'
        app_label = 'common'
